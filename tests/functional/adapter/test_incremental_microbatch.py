import pytest
from dbt.tests.adapter.incremental.test_incremental_microbatch import (
    BaseMicrobatch,
)


@pytest.mark.skip("CrateDB: `MERGE` operation not supported")
class TestPostgresMicrobatch(BaseMicrobatch):
    pass
