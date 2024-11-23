import pytest
from dbt.tests.adapter.empty.test_empty import BaseTestEmpty


@pytest.mark.skip(
    "CrateDB: Couldn't create execution plan, see https://github.com/crate/crate/issues/17051"
)
class TestEmpty(BaseTestEmpty):
    pass
