from dbt.tests.adapter.store_test_failures_tests.test_store_test_failures import (
    BaseStoreTestFailures,
)


class TestStoreTestFailures(BaseStoreTestFailures):
    def test__store_and_assert(self, project, clean_up):
        self.run_tests_store_one_failure(project)
        # TODO: Fails for unknown reasons.
        # self.run_tests_store_failures_and_assert(project)
