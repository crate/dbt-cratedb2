from dataclasses import dataclass
from dbt.adapters.postgres import PostgresRelation

from dbt.adapters.cratedb.relation_configs import (
    MAX_CHARACTERS_IN_IDENTIFIER,
)


@dataclass(frozen=True, eq=False, repr=False)
class CrateDBRelation(PostgresRelation):
    def relation_max_name_length(self):
        return MAX_CHARACTERS_IN_IDENTIFIER
