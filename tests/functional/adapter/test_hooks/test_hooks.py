"""
This file needs to be in its own directory because it uses a `data` directory.
Placing this file in its own directory avoids collisions.
"""

import pytest
from dbt.tests.adapter.hooks.test_model_hooks import (
    BasePrePostModelHooks,
    BaseHookRefs,
    BasePrePostModelHooksOnSeeds,
    BaseHooksRefsOnSeeds,
    BasePrePostModelHooksOnSeedsPlusPrefixed,
    BasePrePostModelHooksOnSeedsPlusPrefixedWhitespace,
    BasePrePostModelHooksOnSnapshots,
    BasePrePostModelHooksInConfig,
    BasePrePostModelHooksInConfigWithCount,
    BasePrePostModelHooksInConfigKwargs,
    BasePrePostSnapshotHooksInConfigKwargs,
    BaseDuplicateHooksInConfigs,
    BaseTestPrePost,
    MODEL_PRE_HOOK,
    MODEL_POST_HOOK,
)
from dbt.tests.adapter.hooks.test_run_hooks import (
    BasePrePostRunHooks,
    BaseAfterRunHooks,
)


class BaseTestPrePostCrateDB(BaseTestPrePost):

    def check_hooks(self, state, project, host, count=1):
        ctxs = self.get_ctx_vars(state, count=count, project=project)
        for ctx in ctxs:
            assert ctx["test_state"] == state
            # FIXME: Well, this gets interpreted as catalog name by CrateDB.
            #        See "dbname": os.getenv("POSTGRES_TEST_DATABASE", "crate")
            #        in `tests/functional/conftest.py`.
            assert ctx["target_dbname"] == "crate"
            assert ctx["target_host"] == host
            assert ctx["target_name"] == "default"
            assert ctx["target_schema"] == project.test_schema
            assert ctx["target_threads"] == 4
            # TODO: Adjustment for CrateDB.
            assert ctx["target_type"] == "cratedb"
            assert ctx["target_user"] == "crate"
            assert ctx["target_pass"] == ""

            assert (
                ctx["run_started_at"] is not None and len(ctx["run_started_at"]) > 0
            ), "run_started_at was not set"
            assert (
                ctx["invocation_id"] is not None and len(ctx["invocation_id"]) > 0
            ), "invocation_id was not set"
            assert ctx["thread_id"].startswith("Thread-")


class BasePrePostModelHooksCrateDB(BasePrePostModelHooks):
    @pytest.fixture(scope="class")
    def project_config_update(self):
        """
        CrateDB: `VACUUM` not supported.
        """
        return {
            "models": {
                "test": {
                    "pre-hook": [
                        # inside transaction (runs second)
                        MODEL_PRE_HOOK,
                        # outside transaction (runs first)
                        # TODO: Adjustment for CrateDB.
                        # {"sql": "vacuum {{ this.schema }}.on_model_hook", "transaction": False},
                        {
                            "sql": "OPTIMIZE TABLE {{ this.schema }}.on_model_hook",
                            "transaction": False,
                        },
                    ],
                    "post-hook": [
                        # outside transaction (runs second)
                        # TODO: Adjustment for CrateDB.
                        # {"sql": "vacuum {{ this.schema }}.on_model_hook", "transaction": False},
                        {
                            "sql": "OPTIMIZE TABLE {{ this.schema }}.on_model_hook",
                            "transaction": False,
                        },
                        # inside transaction (runs first)
                        MODEL_POST_HOOK,
                    ],
                }
            }
        }


class TestPrePostModelHooks(BasePrePostModelHooksCrateDB, BaseTestPrePostCrateDB):
    pass


class TestHookRefs(BaseHookRefs, BaseTestPrePostCrateDB):
    pass


class BasePrePostModelHooksOnSeedsCrateDB(BasePrePostModelHooksOnSeeds):
    pass


class TestPrePostModelHooksOnSeeds(BasePrePostModelHooksOnSeedsCrateDB):
    pass


class TestHooksRefsOnSeeds(BaseHooksRefsOnSeeds):
    pass


class TestPrePostModelHooksOnSeedsPlusPrefixed(
    BasePrePostModelHooksOnSeedsPlusPrefixed,
    BasePrePostModelHooksOnSeedsCrateDB,
):
    pass


class TestPrePostModelHooksOnSeedsPlusPrefixedWhitespace(
    BasePrePostModelHooksOnSeedsPlusPrefixedWhitespace,
    BasePrePostModelHooksOnSeedsCrateDB,
):
    pass


@pytest.mark.skip("FIXME: Fails on CrateDB. Reason unknown.")
class TestPrePostModelHooksOnSnapshots(BasePrePostModelHooksOnSnapshots, BaseTestPrePostCrateDB):
    pass


class TestPrePostModelHooksInConfig(BasePrePostModelHooksInConfig, BaseTestPrePostCrateDB):
    pass


@pytest.mark.skip("FIXME: Fails on CrateDB. Reason unknown.")
class TestPrePostModelHooksInConfigWithCount(
    BasePrePostModelHooksCrateDB,
    BaseTestPrePostCrateDB,
    BasePrePostModelHooksInConfigWithCount,
):
    pass


class TestPrePostModelHooksInConfigKwargs(
    BasePrePostModelHooksInConfigKwargs, BaseTestPrePostCrateDB
):
    pass


@pytest.mark.skip("FIXME: Fails on CrateDB. Reason unknown.")
class TestPrePostSnapshotHooksInConfigKwargs(
    BasePrePostSnapshotHooksInConfigKwargs, BaseTestPrePostCrateDB
):
    pass


class TestDuplicateHooksInConfigs(BaseDuplicateHooksInConfigs):
    pass


class BasePrePostRunHooksCrateDB(BasePrePostRunHooks):
    def check_hooks(self, state, project, host):
        ctx = self.get_ctx_vars(state, project)

        assert ctx["test_state"] == state
        assert ctx["target_dbname"] == "crate"
        assert ctx["target_host"] == host
        assert ctx["target_name"] == "default"
        assert ctx["target_schema"] == project.test_schema
        assert ctx["target_threads"] == 4
        assert ctx["target_type"] == "cratedb"
        assert ctx["target_user"] == "crate"
        assert ctx["target_pass"] == ""

        assert (
            ctx["run_started_at"] is not None and len(ctx["run_started_at"]) > 0
        ), "run_started_at was not set"
        assert (
            ctx["invocation_id"] is not None and len(ctx["invocation_id"]) > 0
        ), "invocation_id was not set"
        assert ctx["thread_id"].startswith("Thread-") or ctx["thread_id"] == "MainThread"


class TestPrePostRunHooks(BasePrePostRunHooksCrateDB):
    pass


class TestAfterRunHooks(BaseAfterRunHooks):
    pass
