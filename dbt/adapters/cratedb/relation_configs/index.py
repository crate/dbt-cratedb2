from dataclasses import dataclass, field
from typing import FrozenSet

from dbt.adapters.postgres.relation_configs import PostgresIndexConfig, PostgresIndexConfigChange
from dbt_common.dataclass_schema import StrEnum


class CrateDBIndexMethod(StrEnum):
    # TODO: Adjust for CrateDB.
    btree = "btree"
    hash = "hash"
    gist = "gist"
    spgist = "spgist"
    gin = "gin"
    brin = "brin"

    @classmethod
    def default(cls) -> "CrateDBIndexMethod":
        return cls("btree")


@dataclass(frozen=True, eq=True, unsafe_hash=True)
class CrateDBIndexConfig(PostgresIndexConfig):
    name: str = field(default="", hash=False, compare=False)
    column_names: FrozenSet[str] = field(default_factory=frozenset, hash=True)
    unique: bool = field(default=False, hash=True)
    method: CrateDBIndexMethod = field(default=CrateDBIndexMethod.default(), hash=True)  # type: ignore[assignment]


@dataclass(frozen=True, eq=True, unsafe_hash=True)
class CrateDBIndexConfigChange(PostgresIndexConfigChange):
    pass
