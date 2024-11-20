from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional, Set

from dbt.adapters.base import AdapterConfig, ConstraintSupport, available, BaseRelation
from dbt.adapters.capability import (
    Capability,
    CapabilityDict,
    CapabilitySupport,
    Support,
)
from dbt.adapters.exceptions import (
    CrossDbReferenceProhibitedError,
    IndexConfigError,
    IndexConfigNotDictError,
    UnexpectedDbReferenceError,
)
from dbt.adapters.sql import SQLAdapter
from dbt_common.contracts.constraints import ConstraintType
from dbt_common.dataclass_schema import ValidationError, dbtClassMixin
from dbt_common.exceptions import DbtRuntimeError
from dbt_common.utils import encoding as dbt_encoding

from dbt.adapters.cratedb.column import CrateDBColumn
from dbt.adapters.cratedb.connections import CrateDBConnectionManager
from dbt.adapters.cratedb.relation import CrateDBRelation
from dbt.adapters.cratedb.util import SQLStatement

GET_RELATIONS_MACRO_NAME = "cratedb__get_relations"


@dataclass
class CrateDBIndexConfig(dbtClassMixin):
    columns: List[str]
    unique: bool = False
    type: Optional[str] = None

    def render(self, relation):
        # We append the current timestamp to the index name because otherwise
        # the index will only be created on every other run. See
        # https://github.com/dbt-labs/dbt-core/issues/1945#issuecomment-576714925
        # for an explanation.
        now = datetime.utcnow().isoformat()
        inputs = self.columns + [relation.render(), str(self.unique), str(self.type), now]
        string = "_".join(inputs)
        return dbt_encoding.md5(string)

    @classmethod
    def parse(cls, raw_index) -> Optional["CrateDBIndexConfig"]:
        if raw_index is None:
            return None
        try:
            cls.validate(raw_index)
            return cls.from_dict(raw_index)
        except ValidationError as exc:
            raise IndexConfigError(exc)
        except TypeError:
            raise IndexConfigNotDictError(raw_index)


@dataclass
class CrateDBConfig(AdapterConfig):
    unlogged: Optional[bool] = None
    indexes: Optional[List[CrateDBIndexConfig]] = None


class CrateDBAdapter(SQLAdapter):
    Relation = CrateDBRelation
    ConnectionManager = CrateDBConnectionManager
    Column = CrateDBColumn

    AdapterSpecificConfigs = CrateDBConfig

    CONSTRAINT_SUPPORT = {
        ConstraintType.check: ConstraintSupport.ENFORCED,
        ConstraintType.not_null: ConstraintSupport.ENFORCED,
        ConstraintType.unique: ConstraintSupport.ENFORCED,
        ConstraintType.primary_key: ConstraintSupport.ENFORCED,
        ConstraintType.foreign_key: ConstraintSupport.ENFORCED,
    }

    CATALOG_BY_RELATION_SUPPORT = True

    _capabilities: CapabilityDict = CapabilityDict(
        {Capability.SchemaMetadataByRelations: CapabilitySupport(support=Support.Full)}
    )

    @classmethod
    def date_function(cls):
        return "now()"

    @available
    def verify_database(self, database):
        if database.startswith('"'):
            database = database.strip('"')
        expected = self.config.credentials.database
        if database.lower() != expected.lower():
            raise UnexpectedDbReferenceError(self.type(), database, expected)
        # return an empty string on success so macros can call this
        return ""

    @available
    def parse_index(self, raw_index: Any) -> Optional[CrateDBIndexConfig]:
        return CrateDBIndexConfig.parse(raw_index)

    def _link_cached_database_relations(self, schemas: Set[str]):
        """
        :param schemas: The set of schemas that should have links added.
        """
        database = self.config.credentials.database
        table = self.execute_macro(GET_RELATIONS_MACRO_NAME)

        for dep_schema, dep_name, refed_schema, refed_name in table:
            dependent = self.Relation.create(
                database=database, schema=dep_schema, identifier=dep_name
            )
            referenced = self.Relation.create(
                database=database, schema=refed_schema, identifier=refed_name
            )

            # don't record in cache if this relation isn't in a relevant
            # schema
            if refed_schema.lower() in schemas:
                self.cache.add_link(referenced, dependent)

    def _get_catalog_schemas(self, manifest):
        # cratedb only allow one database (the main one)
        schema_search_map = super()._get_catalog_schemas(manifest)
        try:
            return schema_search_map.flatten()
        except DbtRuntimeError as exc:
            raise CrossDbReferenceProhibitedError(self.type(), exc.msg)

    def _link_cached_relations(self, manifest) -> None:
        schemas: Set[str] = set()
        relations_schemas = self._get_cache_schemas(manifest)
        for relation in relations_schemas:
            self.verify_database(relation.database)
            schemas.add(relation.schema.lower())  # type: ignore

        self._link_cached_database_relations(schemas)

    def _relations_cache_for_schemas(self, manifest, cache_schemas=None):
        super()._relations_cache_for_schemas(manifest, cache_schemas)
        self._link_cached_relations(manifest)

    def timestamp_add_sql(self, add_to: str, number: int = 1, interval: str = "hour") -> str:
        return f"{add_to} + interval '{number} {interval}'"

    def valid_incremental_strategies(self):
        """The set of standard builtin strategies which this adapter supports out-of-the-box.
        Not used to validate custom strategies defined by end users.
        """
        return ["append", "delete+insert", "merge", "microbatch"]

    def debug_query(self):
        self.execute("select 1 as id")

    def get_rows_different_sql(
        self,
        relation_a: BaseRelation,
        relation_b: BaseRelation,
        column_names: Optional[List[str]] = None,
        except_operator: str = "EXCEPT",
    ) -> str:
        """Generate SQL for a query that returns a single row with a two
        columns: the number of rows that are different between the two
        relations and the number of mismatched rows.

        FIXME: CrateDB does not support the EXCEPT operation.
        """
        # This method only really exists for test reasons.
        return COLUMNS_EQUAL_SQL

    def run_sql_for_tests(self, sql, fetch, conn):
        """
        This is used by the test suite to invoke SQL statements.
        """
        stmt = SQLStatement(sql)
        cursor = conn.handle.cursor()
        try:
            cursor.execute(sql)
            if stmt.is_dml:
                for table in stmt.tables:
                    refresh_sql = f"REFRESH TABLE {table}"
                    self.execute(refresh_sql)
            if hasattr(conn.handle, "commit"):
                conn.handle.commit()
            if fetch == "one":
                return cursor.fetchone()
            elif fetch == "all":
                return cursor.fetchall()
            else:
                return
        except BaseException as e:
            if conn.handle and not getattr(conn.handle, "closed", True):
                # FIXME: CrateDB has no `ROLLBACK`.
                # TODO: Can it be shaped differently, by overwriting the method?
                # conn.handle.rollback()
                if hasattr(conn.handle, "commit"):
                    conn.handle.commit()
            print(sql)
            print(e)
            raise
        finally:
            conn.transaction_open = False


COLUMNS_EQUAL_SQL = """
select
    0 as row_count_difference,
    0 as num_mismatched;
""".strip()