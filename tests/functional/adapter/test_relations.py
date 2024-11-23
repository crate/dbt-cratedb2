import pytest
from dbt.tests.adapter.relations.test_changing_relation_type import BaseChangeRelationTypeValidator
from dbt.tests.adapter.relations.test_dropping_schema_named import BaseDropSchemaNamed


class TestChangeRelationTypes(BaseChangeRelationTypeValidator):
    pass


@pytest.mark.skip("CrateDB: `DROP SCHEMA` not supported")
class TestDropSchemaNamed(BaseDropSchemaNamed):
    pass
