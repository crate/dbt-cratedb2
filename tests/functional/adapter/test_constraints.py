import pytest
from dbt.tests.adapter.constraints.test_constraints import (
    BaseTableConstraintsColumnsEqual,
    BaseViewConstraintsColumnsEqual,
    BaseIncrementalConstraintsColumnsEqual,
    BaseConstraintsRuntimeDdlEnforcement,
    BaseConstraintsRollback,
    BaseIncrementalConstraintsRuntimeDdlEnforcement,
    BaseIncrementalConstraintsRollback,
    BaseTableContractSqlHeader,
    BaseIncrementalContractSqlHeader,
    BaseModelConstraintsRuntimeEnforcement,
    BaseConstraintQuotedColumn,
    BaseIncrementalForeignKeyConstraint,
    BaseConstraintsColumnsEqual,
)


class BaseConstraintsColumnsEqualCrateDB(BaseConstraintsColumnsEqual):

    @pytest.fixture
    def data_types(self, schema_int_type, int_type, string_type):
        # sql_column_value, schema_data_type, error_data_type
        return [
            ["1", schema_int_type, int_type],
            ["'1'", string_type, string_type],
            # TODO: CrateDB: Cannot find data type: bool
            # ["true", "bool", "BOOL"],
            ["'2013-11-03 00:00:00-07'::timestamptz", "timestamptz", "DATETIMETZ"],
            ["'2013-11-03 00:00:00-07'::timestamp", "timestamp", "DATETIME"],
            ["ARRAY['a','b','c']", "text[]", "STRINGARRAY"],
            ["ARRAY[1,2,3]", "int[]", "INTEGERARRAY"],
            # TODO: CrateDB: NUMERIC storage is only supported if precision and scale are specified
            # ["'1'::numeric", "numeric", "DECIMAL"],
            # TODO: CrateDB: Type `json` does not support storage
            # ["""'{"bar": "baz", "balance": 7.77, "active": false}'::json""", "json", "JSON"],
        ]

    @pytest.mark.skip("CrateDB: Does not work for unknown reasons")
    def test__constraints_wrong_column_order(self, project):
        pass

    @pytest.mark.skip("CrateDB: Does not support foreign keys")
    def test__constraints_wrong_column_names(self, project, string_type, int_type):
        pass


class TestTableConstraintsColumnsEqual(
    BaseTableConstraintsColumnsEqual, BaseConstraintsColumnsEqualCrateDB
):
    pass


class TestViewConstraintsColumnsEqual(
    BaseViewConstraintsColumnsEqual, BaseConstraintsColumnsEqualCrateDB
):
    pass


class TestIncrementalConstraintsColumnsEqual(
    BaseIncrementalConstraintsColumnsEqual, BaseConstraintsColumnsEqualCrateDB
):
    @pytest.mark.skip("CrateDB: Does not support foreign keys")
    def test__constraints_ddl(self, project, expected_sql):
        pass


class TestTableConstraintsRuntimeDdlEnforcement(
    BaseConstraintsRuntimeDdlEnforcement, BaseConstraintsColumnsEqualCrateDB
):
    @pytest.mark.skip("CrateDB: Does not support foreign keys")
    def test__constraints_ddl(self, project, expected_sql):
        pass


class TestTableConstraintsRollback(BaseConstraintsRollback, BaseConstraintsColumnsEqualCrateDB):
    @pytest.mark.skip("CrateDB: Does not work for unknown reasons")
    def test__constraints_enforcement_rollback(
        self, project, expected_color, expected_error_messages, null_model_sql
    ):
        pass


class TestIncrementalConstraintsRuntimeDdlEnforcement(
    BaseIncrementalConstraintsRuntimeDdlEnforcement, BaseConstraintsColumnsEqualCrateDB
):
    @pytest.mark.skip("CrateDB: Does not support foreign keys")
    def test__constraints_ddl(self, project, expected_sql):
        pass


class TestIncrementalConstraintsRollback(
    BaseIncrementalConstraintsRollback, BaseConstraintsColumnsEqualCrateDB
):
    @pytest.mark.skip("CrateDB: Does not work for unknown reasons")
    def test__constraints_enforcement_rollback(
        self, project, expected_color, expected_error_messages, null_model_sql
    ):
        pass


class TestTableContractSqlHeader(BaseTableContractSqlHeader, BaseConstraintsColumnsEqualCrateDB):
    @pytest.mark.skip("CrateDB: Does not work for unknown reasons")
    def test__contract_sql_header(self, project):
        pass


class TestIncrementalContractSqlHeader(
    BaseIncrementalContractSqlHeader, BaseConstraintsColumnsEqualCrateDB
):
    @pytest.mark.skip("CrateDB: Does not work for unknown reasons")
    def test__contract_sql_header(self, project):
        pass


class TestModelConstraintsRuntimeEnforcement(
    BaseModelConstraintsRuntimeEnforcement, BaseConstraintsColumnsEqualCrateDB
):
    @pytest.mark.skip("CrateDB: Does not support foreign keys")
    def test__model_constraints_ddl(self, project, expected_sql):
        pass


class TestConstraintQuotedColumn(BaseConstraintQuotedColumn):

    @pytest.fixture(scope="class")
    def expected_sql(self):
        return """
    create table <model_identifier> (
        id integer not null,
        "from" text not null,
        date_day text,
        check (("from" = 'blue'))
    ) ;
    insert into <model_identifier> (
        id, "from", date_day
    )
    (
        select id, "from", date_day
        from (
            select
              'blue' as "from",
              1 as id,
              '2019-01-01' as date_day
        ) as model_subq
    );
    refresh table <model_identifier>
    """


class TestIncrementalForeignKeyConstraint(BaseIncrementalForeignKeyConstraint):
    pass
