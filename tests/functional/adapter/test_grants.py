import pytest
from dbt.tests.adapter.grants.test_incremental_grants import BaseIncrementalGrants
from dbt.tests.adapter.grants.test_invalid_grants import BaseInvalidGrants
from dbt.tests.adapter.grants.test_model_grants import BaseModelGrants
from dbt.tests.adapter.grants.test_seed_grants import BaseSeedGrants
from dbt.tests.adapter.grants.test_snapshot_grants import BaseSnapshotGrants

pytest.skip("CrateDB: Does not work for various reasons", allow_module_level=True)


class TestIncrementalGrants(BaseIncrementalGrants):
    pass


class TestInvalidGrants(BaseInvalidGrants):
    pass


class TestModelGrants(BaseModelGrants):
    pass


class TestSeedGrants(BaseSeedGrants):
    pass


class TestSnapshotGrants(BaseSnapshotGrants):
    pass
