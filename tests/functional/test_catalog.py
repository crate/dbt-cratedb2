import pytest
from dbt.tests.adapter.catalog.relation_types import CatalogRelationTypes


@pytest.mark.skip("CrateDB: MATERIALIZED VIEW not supported")
class TestCatalogRelationTypes(CatalogRelationTypes):
    pass
