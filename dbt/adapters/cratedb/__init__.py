from dbt.adapters.base import AdapterPlugin

from dbt.adapters.cratedb.column import CrateDBColumn
from dbt.adapters.cratedb.connections import (
    CrateDBConnectionManager,
    CrateDBCredentials,
)
from dbt.adapters.cratedb.impl import CrateDBAdapter
from dbt.adapters.cratedb.relation import CrateDBRelation
from dbt.include import cratedb


Plugin = AdapterPlugin(
    adapter=CrateDBAdapter,  # type: ignore
    credentials=CrateDBCredentials,
    include_path=cratedb.PACKAGE_PATH,
    dependencies=["postgres"],
)
