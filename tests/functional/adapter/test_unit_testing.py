import pytest
from dbt.tests.adapter.unit_testing.test_case_insensitivity import BaseUnitTestCaseInsensivity
from dbt.tests.adapter.unit_testing.test_invalid_input import BaseUnitTestInvalidInput
from dbt.tests.adapter.unit_testing.test_types import BaseUnitTestingTypes


class TestPostgresUnitTestCaseInsensitivity(BaseUnitTestCaseInsensivity):
    pass


class TestPostgresUnitTestInvalidInput(BaseUnitTestInvalidInput):
    pass


class TestCrateDBUnitTestingTypes(BaseUnitTestingTypes):
    @pytest.fixture
    def data_types(self):
        # sql_value, yaml_value
        return [
            ["1", "1"],
            ["'1'", "1"],
            ["true", "true"],
            # TODO: CrateDB: Type `date` does not support storage
            # ["DATE '2020-01-02'", "2020-01-02"],
            ["TIMESTAMP '2013-11-03 00:00:00-0000'", "2013-11-03 00:00:00-0000"],
            ["TIMESTAMPTZ '2013-11-03 00:00:00-0000'", "2013-11-03 00:00:00-0000"],
            # TODO: CrateDB: NUMERIC storage is only supported if precision and scale are specified
            # ["'1'::numeric", "1"],
            # TODO: CrateDB: Type `json` does not support storage
            # [
            #     """'{"bar": "baz", "balance": 7.77, "active": false}'::json""",
            #     """'{"bar": "baz", "balance": 7.77, "active": false}'""",
            # ],
            # TODO: support complex types
            # ["ARRAY['a','b','c']", """'{"a", "b", "c"}'"""],
            # ["ARRAY[1,2,3]", """'{1, 2, 3}'"""],
        ]
