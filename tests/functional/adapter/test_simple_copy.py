import pytest
from dbt.tests.adapter.simple_copy.test_copy_uppercase import BaseSimpleCopyUppercase
from dbt.tests.adapter.simple_copy.test_simple_copy import (
    SimpleCopyBase,
    EmptyModelsArentRunBase,
)


class TestSimpleCopyUppercase(BaseSimpleCopyUppercase):
    @pytest.fixture(scope="class")
    def dbt_profile_target(self):
        return {
            "type": "postgres",
            "threads": 4,
            "host": "localhost",
            "port": 5432,
            "user": "crate",
            "pass": "password",
            "dbname": "dbtMixedCase",
        }


class TestSimpleCopyBase(SimpleCopyBase):

    @pytest.mark.skip("CrateDB: MATERIALIZED VIEW not supported")
    def test_simple_copy_with_materialized_views(self, project):
        pass


class TestEmptyModelsArentRun(EmptyModelsArentRunBase):
    pass
