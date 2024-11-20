import os

import pytest

from tests.functional.projects import dbt_integration


@pytest.fixture(scope="class")
def dbt_integration_project():
    return dbt_integration()


@pytest.fixture(scope="class")
def dbt_profile_target():
    return {
        "type": "cratedb",
        "host": os.getenv("POSTGRES_TEST_HOST", "localhost"),
        "port": int(os.getenv("POSTGRES_TEST_PORT", 5432)),
        "user": os.getenv("POSTGRES_TEST_USER", "crate"),
        "pass": os.getenv("POSTGRES_TEST_PASS", ""),
        # FIXME: Well, this gets interpreted as catalog name by CrateDB.
        #        For now, just accept it as c'est la vie?
        #        For the future, let's revisit this again?
        "dbname": os.getenv("POSTGRES_TEST_DATABASE", "crate"),
        "threads": int(os.getenv("POSTGRES_TEST_THREADS", 4)),
    }


@pytest.fixture(scope="class")
def profile_user(dbt_profile_target):
    # Adjusted for CrateDB. FIXME: Why?
    return "unknown (OID=0)"
