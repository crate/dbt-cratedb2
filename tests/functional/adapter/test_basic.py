import pytest
from dbt.tests.adapter.basic.test_adapter_methods import BaseAdapterMethod
from dbt.tests.adapter.basic.test_base import BaseSimpleMaterializations
from dbt.tests.adapter.basic.test_docs_generate import (
    BaseDocsGenerate,
    BaseDocsGenReferences,
)
from dbt.tests.adapter.basic.test_empty import BaseEmpty
from dbt.tests.adapter.basic.test_ephemeral import BaseEphemeral
from dbt.tests.adapter.basic.test_generic_tests import BaseGenericTests
from dbt.tests.adapter.basic.test_incremental import (
    BaseIncremental,
    BaseIncrementalNotSchemaChange,
    BaseIncrementalBadStrategy,
)
from dbt.tests.adapter.basic.test_singular_tests import BaseSingularTests
from dbt.tests.adapter.basic.test_singular_tests_ephemeral import BaseSingularTestsEphemeral
from dbt.tests.adapter.basic.test_snapshot_check_cols import BaseSnapshotCheckCols
from dbt.tests.adapter.basic.test_snapshot_timestamp import BaseSnapshotTimestamp
from dbt.tests.adapter.basic.test_table_materialization import BaseTableMaterialization
from dbt.tests.adapter.basic.test_validate_connection import BaseValidateConnection


models__model_sql = """

{% set upstream = ref('upstream') %}

{% if execute %}
    {# don't ever do any of this #}

    {# FIXME: CrateDB does not understand `DROP SCHEMA` yet #}
    {%- do adapter.drop_schema(upstream) -%}

    {# FIXME: CrateDB workaround #}
    {% set table_fqn = adapter.get_relation(upstream.database, upstream.schema, upstream.identifier) %}
    {%- do drop_relation_if_exists(table_fqn) -%}

    {% set existing = adapter.get_relation(upstream.database, upstream.schema, upstream.identifier) %}
    {% if existing is not none %}
        {% do exceptions.raise_compiler_error('expected ' ~ ' to not exist, but it did') %}
    {% endif %}

    {%- do adapter.create_schema(upstream) -%}

    {% set sql = create_view_as(upstream, 'select 2 as id') %}
    {% do run_query(sql) %}
{% endif %}


select * from {{ upstream }}

"""


class TestBaseCaching(BaseAdapterMethod):
    @pytest.fixture(scope="class")
    def models(self):
        from dbt.tests.adapter.basic.test_adapter_methods import (
            models__upstream_sql,
            models__expected_sql,
        )

        return {
            "upstream.sql": models__upstream_sql,
            "expected.sql": models__expected_sql,
            "model.sql": models__model_sql,
        }


class TestSimpleMaterializations(BaseSimpleMaterializations):
    pass


class TestDocsGenerate(BaseDocsGenerate):
    pass


class TestDocsGenReferences(BaseDocsGenReferences):
    pass


class TestEmpty(BaseEmpty):
    pass


class TestEphemeral(BaseEphemeral):
    pass


class TestGenericTests(BaseGenericTests):
    pass


class TestIncremental(BaseIncremental):
    pass


class TestBaseIncrementalNotSchemaChange(BaseIncrementalNotSchemaChange):
    pass


class TestBaseIncrementalBadStrategy(BaseIncrementalBadStrategy):
    pass


class TestSingularTests(BaseSingularTests):
    pass


class TestSingularTestsEphemeral(BaseSingularTestsEphemeral):
    pass


@pytest.mark.skip("Snapshots not implemented yet")
class TestSnapshotCheckCols(BaseSnapshotCheckCols):
    pass


@pytest.mark.skip("Snapshots not implemented yet")
class TestSnapshotTimestamp(BaseSnapshotTimestamp):
    pass


class TestTableMat(BaseTableMaterialization):
    pass


class TestValidateConnection(BaseValidateConnection):
    pass
