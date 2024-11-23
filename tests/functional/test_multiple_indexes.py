import pytest

from tests.functional.utils import run_dbt


REF_MULTIPLE_INDEX_MODEL = """
{{
    config(
        materialized="materialized_view",
        indexes=[
            {"columns": ["foo"], "type": "btree"},
            {"columns": ["bar"], "type": "btree"},
        ],
    )
}}

SELECT 1 AS foo, 2 AS bar
"""


@pytest.mark.skip("CrateDB: MATERIALIZED VIEW not supported")
class TestUnrestrictedPackageAccess:
    @pytest.fixture(scope="class")
    def models(self):
        return {"index_test.sql": REF_MULTIPLE_INDEX_MODEL}

    def test_unrestricted_protected_ref(self, project):
        run_dbt()
