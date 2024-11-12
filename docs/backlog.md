# dbt-cratedb2 backlog

## Bugs?
- [o] 'Database Error\n  Validation Failed: 1: this action would add [4] total shards, but this cluster currently has [1000]/[1000] maximum shards open;
   ```
   [2024-11-12T02:02:47,562][INFO ][i.c.m.c.RenameTableClusterStateExecutor] [Olperer] renaming table 'test17313769673008283614_test_basic.ephemeral_summary__dbt_tmp' to 'test17313769673008283614_test_basic.ephemeral_summary'
   [2024-11-12T02:02:47,677][INFO ][o.e.c.r.a.AllocationService] [Olperer] Cluster health status changed from [RED] to [GREEN] (reason: [shards started [[test17313769673008283614_test_basic.ephemeral_summary][3], [test17313769673008283614_test_basic.ephemeral_summary][2], [test17313769673008283614_test_basic.ephemeral_summary][1], [test17313769673008283614_test_basic.ephemeral_summary][0]]]).
   ```

## Testing
From `release-internal.yml` GHA workflow.
```shell
python -c "import dbt.adapters.cratedb"
```

## Testing (from upstream)

###  Goals of moving tests to pytest
* Readability
* Modularity
* Easier to create and debug
* Ability to create a project for external debugging

### TODO
* Create the ability to export a project
* Explore using:
  *  https://github.com/pytest-docker-compose/pytest-docker-compose or
  *  https://github.com/avast/pytest-docker for automatically managing a CrateDB instance running in a docker container
* Track test coverage (https://pytest-cov.readthedocs.io/en/latest)
