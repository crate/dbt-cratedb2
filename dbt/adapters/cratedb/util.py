import sqlparse
import sql_metadata

import typing as t


class SQLStatement:
    def __init__(self, sql: str):
        self.sql = sql

    @property
    def is_dml(self) -> bool:
        parsed = sqlparse.parse(self.sql)[0]
        return str(parsed.get_type()).upper() in ["INSERT", "UPDATE", "DELETE"]

    @property
    def tables(self) -> t.List[str]:
        """
        - https://github.com/andialbrecht/sqlparse/blob/master/examples/extract_table_names.py
        - https://stackoverflow.com/questions/60822203/how-to-parse-any-sql-get-columns-names-and-table-name-using-sql-parser-in-python
        - https://groups.google.com/forum/#!forum/sqlparse/browse_thread/thread/b0bd9a022e9d4895
        """
        return sql_metadata.Parser(self.sql).tables
