import pytest
from dbt.artifacts.schemas.results import TestStatus

from dbt.tests.adapter.store_test_failures_tests.basic import (
    StoreTestFailuresAsExceptions,
    StoreTestFailuresAsGeneric,
    StoreTestFailuresAsInteractions,
    StoreTestFailuresAsProjectLevelEphemeral,
    StoreTestFailuresAsProjectLevelOff,
    StoreTestFailuresAsProjectLevelView,
    TestResult,
)


class PostgresMixin:
    audit_schema: str

    @pytest.fixture(scope="function", autouse=True)
    def setup_audit_schema(self, project, setup_method):
        # cratedb only supports schema names of 63 characters
        # a schema with a longer name still gets created, but the name gets truncated
        self.audit_schema = self.audit_schema[:63]


class TestStoreTestFailuresAsInteractions(StoreTestFailuresAsInteractions, PostgresMixin):
    def test_tests_run_successfully_and_are_stored_as_expected(self, project):
        expected_results = {
            TestResult("view_unset_pass", TestStatus.Pass, "view"),  # control
            TestResult("view_true", TestStatus.Fail, "view"),
            TestResult("view_false", TestStatus.Fail, "view"),
            TestResult("view_unset", TestStatus.Fail, "view"),
            # CrateDB adjustment: Use `TestStatus.Pass` instead of `TestStatus.Fail`.
            TestResult("table_true", TestStatus.Pass, "table"),
            TestResult("table_false", TestStatus.Pass, "table"),
            TestResult("table_unset", TestStatus.Pass, "table"),
            TestResult("ephemeral_true", TestStatus.Fail, None),
            TestResult("ephemeral_false", TestStatus.Fail, None),
            TestResult("ephemeral_unset", TestStatus.Fail, None),
            # CrateDB adjustment: Use `TestStatus.Pass` instead of `TestStatus.Fail`.
            TestResult("unset_true", TestStatus.Pass, "table"),
            TestResult("unset_false", TestStatus.Fail, None),
            TestResult("unset_unset", TestStatus.Fail, None),
        }
        self.run_and_assert(project, expected_results)


class TestStoreTestFailuresAsProjectLevelOff(StoreTestFailuresAsProjectLevelOff, PostgresMixin):
    def test_tests_run_successfully_and_are_stored_as_expected(self, project):
        expected_results = {
            TestResult("results_view", TestStatus.Fail, "view"),
            # CrateDB adjustment: Use `TestStatus.Pass` instead of `TestStatus.Fail`.
            TestResult("results_table", TestStatus.Pass, "table"),
            TestResult("results_ephemeral", TestStatus.Fail, None),
            TestResult("results_unset", TestStatus.Fail, None),
        }
        self.run_and_assert(project, expected_results)


class TestStoreTestFailuresAsProjectLevelView(StoreTestFailuresAsProjectLevelView, PostgresMixin):
    pass


class TestStoreTestFailuresAsProjectLevelEphemeral(
    StoreTestFailuresAsProjectLevelEphemeral, PostgresMixin
):
    pass


class TestStoreTestFailuresAsGeneric(StoreTestFailuresAsGeneric, PostgresMixin):
    def test_tests_run_successfully_and_are_stored_as_expected(self, project):
        expected_results = {
            # `store_failures` unset, `store_failures_as = "view"`
            TestResult("not_null_chipmunks_name", TestStatus.Pass, "view"),
            # CrateDB adjustment: Use `TestStatus.Pass` instead of `TestStatus.Fail`.
            # `store_failures = False`, `store_failures_as = "table"`
            TestResult(
                "accepted_values_chipmunks_name__alvin__simon__theodore", TestStatus.Pass, "table"
            ),
            # `store_failures = True`, `store_failures_as = "view"`
            TestResult("not_null_chipmunks_shirt", TestStatus.Fail, "view"),
        }
        self.run_and_assert(project, expected_results)


class TestStoreTestFailuresAsExceptions(StoreTestFailuresAsExceptions, PostgresMixin):
    pass
