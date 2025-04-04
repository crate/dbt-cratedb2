from contextlib import contextmanager
from dataclasses import dataclass
from multiprocessing.context import SpawnContext
from typing import Union

from dbt.adapters.contracts.connection import (
    AdapterResponse,
    AdapterRequiredConfig,
)
from dbt.adapters.events.logging import AdapterLogger
from dbt.adapters.events.types import TypeCodeNotFound
from dbt.adapters.postgres import PostgresCredentials

from dbt.adapters.sql import SQLConnectionManager
from dbt_common.exceptions import DbtDatabaseError, DbtRuntimeError
from dbt_common.events.functions import warn_or_error
from dbt_common.record import get_record_mode_from_env, RecorderMode
import psycopg2

from dbt.adapters.cratedb.record.handle import CrateDBRecordReplayHandle
from dbt.adapters.cratedb.util import SQLStatement

logger = AdapterLogger("CrateDB")


@dataclass
class CrateDBCredentials(PostgresCredentials):

    @property
    def type(self):
        return "cratedb"


class CrateDBConnectionManager(SQLConnectionManager):
    TYPE = "cratedb"

    def __init__(self, config: AdapterRequiredConfig, mp_context: SpawnContext) -> None:
        super().__init__(config, mp_context)

    def begin(self):
        pass

    def commit(self):
        pass

    @contextmanager
    def exception_handler(self, sql):
        try:
            # CrateDB: This is a good spot for tracing SQL statements.
            # print("SQL:", sql)
            yield
            # CrateDB needs write synchronization after DML operations.
            # TODO: Only enable optionally?
            stmt = SQLStatement(sql)
            if stmt.is_dml:
                try:
                    for table in stmt.tables:
                        refresh_sql = f"REFRESH TABLE {table}"
                        try:
                            self.execute(refresh_sql)
                        except Exception:
                            pass
                except ValueError as ex:
                    logger.warning(ex)

        except psycopg2.DatabaseError as e:
            logger.debug("CrateDB error: {}".format(str(e)))

            try:
                self.rollback_if_open()
            except psycopg2.Error:
                logger.debug("Failed to release connection!")
                pass

            raise DbtDatabaseError(str(e).strip()) from e

        except Exception as e:
            logger.debug("Error running SQL: {}", sql)
            logger.debug("Rolling back transaction.")
            self.rollback_if_open()
            if isinstance(e, DbtRuntimeError):
                # during a sql query, an internal to dbt exception was raised.
                # this sounds a lot like a signal handler and probably has
                # useful information, so raise it without modification.
                raise

            raise DbtRuntimeError(e) from e

    @classmethod
    def open(cls, connection):
        if connection.state == "open":
            logger.debug("Connection is already open, skipping open.")
            return connection

        credentials = cls.get_credentials(connection.credentials)
        kwargs = {}
        # we don't want to pass 0 along to connect() as cratedb will try to
        # call an invalid setsockopt() call (contrary to the docs).
        if credentials.keepalives_idle:
            kwargs["keepalives_idle"] = credentials.keepalives_idle

        # psycopg2 doesn't support search_path officially,
        # see https://github.com/psycopg/psycopg2/issues/465
        search_path = credentials.search_path
        if search_path is not None and search_path != "":
            # see https://postgresql.org/docs/9.5/libpq-connect.html
            kwargs["options"] = "-c search_path={}".format(search_path.replace(" ", "\\ "))

        if credentials.sslmode:
            kwargs["sslmode"] = credentials.sslmode

        if credentials.sslcert is not None:
            kwargs["sslcert"] = credentials.sslcert

        if credentials.sslkey is not None:
            kwargs["sslkey"] = credentials.sslkey

        if credentials.sslrootcert is not None:
            kwargs["sslrootcert"] = credentials.sslrootcert

        if credentials.application_name:
            kwargs["application_name"] = credentials.application_name

        def connect():
            handle = None

            # In replay mode, we won't connect to a real database at all, while
            # in record and diff modes we do, but insert an intermediate handle
            # object which monitors native connection activity.
            rec_mode = get_record_mode_from_env()
            if rec_mode != RecorderMode.REPLAY:
                handle = psycopg2.connect(
                    dbname=credentials.database,
                    user=credentials.user,
                    host=credentials.host,
                    password=credentials.password,
                    port=credentials.port,
                    connect_timeout=credentials.connect_timeout,
                    **kwargs,
                )

            if rec_mode is not None:
                # If using the record/replay mechanism, regardless of mode, we
                # use a wrapper.
                handle = CrateDBRecordReplayHandle(handle, connection)

            if credentials.role:
                handle.cursor().execute("set role {}".format(credentials.role))

            return handle

        retryable_exceptions = [
            # OperationalError is subclassed by all psycopg2 Connection Exceptions and it's raised
            # by generic connection timeouts without an error code. This is a limitation of
            # psycopg2 which doesn't provide subclasses for errors without a SQLSTATE error code.
            # The limitation has been known for a while and there are no efforts to tackle it.
            # See: https://github.com/psycopg/psycopg2/issues/682
            psycopg2.errors.OperationalError,
        ]

        def exponential_backoff(attempt: int):
            return attempt * attempt

        return cls.retry_connection(
            connection,
            connect=connect,
            logger=logger,
            retry_limit=credentials.retries,
            retry_timeout=exponential_backoff,
            retryable_exceptions=retryable_exceptions,
        )

    def cancel(self, connection):
        connection_name = connection.name
        try:
            pid = connection.handle.get_backend_pid()
        except psycopg2.InterfaceError as exc:
            # if the connection is already closed, not much to cancel!
            if "already closed" in str(exc):
                logger.debug(f"Connection {connection_name} was already closed")
                return
            # probably bad, re-raise it
            raise

        sql = "select pg_terminate_backend({})".format(pid)

        logger.debug("Cancelling query '{}' ({})".format(connection_name, pid))

        _, cursor = self.add_query(sql)
        res = cursor.fetchone()

        logger.debug("Cancel query '{}': {}".format(connection_name, res))

    @classmethod
    def get_credentials(cls, credentials):
        return credentials

    @classmethod
    def get_response(cls, cursor) -> AdapterResponse:
        message = str(cursor.statusmessage)
        rows = cursor.rowcount
        status_message_parts = message.split() if message is not None else []
        status_messsage_strings = [part for part in status_message_parts if not part.isdigit()]
        code = " ".join(status_messsage_strings)
        return AdapterResponse(_message=message, code=code, rows_affected=rows)

    @classmethod
    def data_type_code_to_name(cls, type_code: Union[int, str]) -> str:
        if type_code in psycopg2.extensions.string_types:
            return psycopg2.extensions.string_types[type_code].name
        else:
            warn_or_error(TypeCodeNotFound(type_code=type_code))
            return f"unknown type_code {type_code}"
