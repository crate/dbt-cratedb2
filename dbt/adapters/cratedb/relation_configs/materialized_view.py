from dataclasses import dataclass

from dbt.adapters.postgres.relation_configs import (
    PostgresMaterializedViewConfigChangeCollection,
    PostgresMaterializedViewConfig,
)


@dataclass(frozen=True, eq=True, unsafe_hash=True)
class CrateDBMaterializedViewConfig(PostgresMaterializedViewConfig):
    pass


@dataclass
class CrateDBMaterializedViewConfigChangeCollection(
    PostgresMaterializedViewConfigChangeCollection
):
    pass
