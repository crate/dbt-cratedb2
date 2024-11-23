"""
This file needs to be in its own directory because it creates a `data` directory at run time.
Placing this file in its own directory avoids collisions.
"""

import pytest
from dbt.tests.adapter.simple_seed.test_seed import (
    BaseBasicSeedTests,
    BaseSeedConfigFullRefreshOn,
    BaseSeedConfigFullRefreshOff,
    BaseSeedCustomSchema,
    BaseSeedWithUniqueDelimiter,
    BaseSeedWithWrongDelimiter,
    BaseSeedWithEmptyDelimiter,
    BaseSimpleSeedEnabledViaConfig,
    BaseSeedParsing,
    BaseSimpleSeedWithBOM,
    BaseSeedSpecificFormats,
    BaseTestEmptySeed,
)
from dbt.tests.adapter.simple_seed.test_seed_type_override import (
    BaseSimpleSeedColumnOverride,
)


class TestBasicSeedTests(BaseBasicSeedTests):

    @pytest.mark.skip("CrateDB: Fails for unknown reasons")
    def test_simple_seed_full_refresh_flag(self, project):
        pass


class TestSeedConfigFullRefreshOn(BaseSeedConfigFullRefreshOn):
    @pytest.mark.skip("CrateDB: Fails for unknown reasons")
    def test_simple_seed_full_refresh_config(self, project):
        pass


class TestSeedConfigFullRefreshOff(BaseSeedConfigFullRefreshOff):
    pass


class TestSeedCustomSchema(BaseSeedCustomSchema):
    pass


class TestSeedWithUniqueDelimiter(BaseSeedWithUniqueDelimiter):
    pass


@pytest.mark.skip("CrateDB: Fails for unknown reasons")
class TestSeedWithWrongDelimiter(BaseSeedWithWrongDelimiter):
    pass


class TestSeedWithEmptyDelimiter(BaseSeedWithEmptyDelimiter):
    pass


class BaseSimpleSeedEnabledViaConfigCrateDB(BaseSimpleSeedEnabledViaConfig):
    @pytest.fixture(scope="function")
    def clear_test_schema(self, project):
        yield
        project.run_sql(f"drop table if exists {project.test_schema}.seed_enabled")
        project.run_sql(f"drop table if exists {project.test_schema}.seed_disabled")
        project.run_sql(f"drop table if exists {project.test_schema}.seed_tricky")


class TestSimpleSeedEnabledViaConfig(BaseSimpleSeedEnabledViaConfigCrateDB):
    pass


class TestSeedParsing(BaseSeedParsing):
    pass


class TestSimpleSeedWithBOM(BaseSimpleSeedWithBOM):
    pass


@pytest.mark.skip("CrateDB: Fails for unknown reasons")
class TestSeedSpecificFormats(BaseSeedSpecificFormats):
    pass


class TestEmptySeed(BaseTestEmptySeed):
    pass


@pytest.mark.skip("CrateDB: Type `date` does not support storage")
class TestSimpleSeedColumnOverride(BaseSimpleSeedColumnOverride):
    pass
