import pytest
from dbt.tests.adapter.dbt_show.test_dbt_show import (
    BaseShowLimit,
    BaseShowSqlHeader,
    BaseShowDoesNotHandleDoubleLimit,
)


class TestPostgresShowSqlHeader(BaseShowSqlHeader):
    pass


class TestPostgresShowLimit(BaseShowLimit):
    pass


@pytest.mark.skip("CrateDB: mismatched input 'limit' expecting {<EOF>, ';'}")
class TestPostgresShowDoesNotHandleDoubleLimit(BaseShowDoesNotHandleDoubleLimit):
    pass
