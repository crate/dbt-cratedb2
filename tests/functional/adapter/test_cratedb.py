import pytest
from dbt.tests.adapter.simple_snapshot import common

from dbt.tests.util import check_relations_equal, run_dbt


basic_sql = """
SELECT 42
"""

rename_table_sql = """
{% set exists, table_source = get_or_create_relation(database=None, schema=target.schema, identifier="table_source", type="table") %}
{% set exists, table_target = get_or_create_relation(database=None, schema=target.schema, identifier="table_target", type="table") %}

{# Create table `source`. #}
{% set sql = get_create_table_as_sql(False, table_source, "SELECT 42 as value") %}
{% do run_query(sql) %}

{# Rename table to `target`. #}
{% do adapter.rename_relation(table_source, table_target) %}

-- Dummy statement.
SELECT TRUE
"""


rename_view_sql = """
{% set exists, view_source = get_or_create_relation(database=None, schema=target.schema, identifier="view_source", type="view") %}
{% set exists, view_target = get_or_create_relation(database=None, schema=target.schema, identifier="view_target", type="view") %}

{# Create view `source`. #}
{% set sql = get_create_view_as_sql(view_source, "SELECT 42 as value") %}
{% do run_query(sql) %}

{# Rename view to `target`. #}
{% do adapter.rename_relation(view_source, view_target) %}

-- Dummy statement.
SELECT TRUE
"""


reset_csv_table = """
{# Create a random table. #}
{% set exists, random_table = get_or_create_relation(database=None, schema=target.schema, identifier="random_table", type="table") %}
{% set sql = get_create_table_as_sql(False, random_table, "SELECT 42 as value") %}
{% do run_query(sql) %}

{#
This is a little excerpt from dbt/include/global_project/macros/materializations/seeds/seed.sql
#}
{% set full_refresh = (should_full_refresh()) %}
{% set agate_table = None %}
{% set sql_ddl = reset_csv_table(model=model, full_refresh=full_refresh, old_relation=random_table, agate_table=agate_table) %}
{% set sql_dml = load_csv_rows(model, agate_table) %}
{% set sql = get_csv_sql(sql_ddl, sql_dml) %}
{% do run_query(sql) %}

SELECT TRUE
"""


class TestCrateDB:
    """
    A few test cases for specifically validating concerns of CrateDB.
    """

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "basic.sql": basic_sql,
            "rename_table.sql": rename_table_sql,
            "rename_view.sql": rename_view_sql,
            "reset_csv_table.sql": reset_csv_table,
        }

    @pytest.fixture(autouse=True)
    def clean_up(self, project):
        """
        TODO: The standard way of cleaning up resources probably does not work,
              because `drop_schema` is not implemented, and has been made a no-op.
        """
        yield
        with project.adapter.connection_named("__test"):
            relation = project.adapter.Relation.create(
                database=project.database, schema=project.test_schema
            )
            project.adapter.drop_schema(relation)

    def test_basic(self, project):
        """
        Validate a basic dbt run.
        """

        result = run_dbt(["run", "--select", "basic"])
        assert len(result) == 1

        # FIXME: Seems to do nothing. Most probably, because `impl.py::get_rows_different_sql`
        #        does not work, because `EXCEPT` support is missing?
        check_relations_equal(project.adapter, ["basic", "foobar"])

        records = common.get_records(project, "basic")
        assert records == [(42,)]

    def test_rename_relation_table(self, project):
        """
        Validate the vanilla `rename_relation` macro from dbt-postgres on tables.
        """

        result = run_dbt(["run", "--select", "rename_table"])
        assert len(result) == 1

        records = common.get_records(project, "table_target")
        assert records == [(42,)]

    def test_rename_relation_view(self, project):
        """
        Validate the vanilla `rename_relation` macro from dbt-postgres on views.
        """

        result = run_dbt(["run", "--select", "rename_view"])
        assert len(result) == 1

        records = common.get_records(project, "view_target")
        assert records == [(42,)]

    def test_reset_csv(self, project):
        """
        CrateDB needs an override for the `reset_csv_table` macro. Make sure it is in place.
        """

        result = run_dbt(["run", "--select", "reset_csv_table"])
        assert len(result) == 1

        records = common.get_records(project, "reset_csv_table")
        assert records == [(True,)]
