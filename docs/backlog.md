# dbt-cratedb2 backlog

## Iteration +1
- Fix column generation when using `OBJECT` types.
  https://github.com/crate/dbt-cratedb2/issues/10
- Investigate the need for generate_schema_name
  https://github.com/crate/dbt-cratedb2/issues/5
- Make write synchronization only optional?
- Bug? 'Database Error\n  Validation Failed: 1: this action would add [4] total shards, but this cluster currently has [1000]/[1000] maximum shards open;
  ```
  [2024-11-12T02:02:47,562][INFO ][i.c.m.c.RenameTableClusterStateExecutor] [Olperer] renaming table 'test17313769673008283614_test_basic.ephemeral_summary__dbt_tmp' to 'test17313769673008283614_test_basic.ephemeral_summary'
  [2024-11-12T02:02:47,677][INFO ][o.e.c.r.a.AllocationService] [Olperer] Cluster health status changed from [RED] to [GREEN] (reason: [shards started [[test17313769673008283614_test_basic.ephemeral_summary][3], [test17313769673008283614_test_basic.ephemeral_summary][2], [test17313769673008283614_test_basic.ephemeral_summary][1], [test17313769673008283614_test_basic.ephemeral_summary][0]]]).
  ```

## Iteration +2
- After CrateDB can do materialized views, the feature can be added to the adapter.
- When CrateDB can do materialized views, it may weigh in as a first citizen of the
  ecosystem, so the adapter may become a dbt [trusted adapter], which provides a few
  benefits. [What it means to be trusted] enumerates the relevant criteria.
- Add dedicated "cratedb-configs" page to upstream documentation
  https://github.com/crate/dbt-cratedb2/issues/7
- The [CrateDB and dbt documentation page] may be improved, specifically outlining
  caveats and differences when comparing PostgreSQL's capabilities with CrateDB's,
  and by adding a high-level overview about the feature capabilities of `dbt-cratedb2`,
  to get expectations right and visible from the very beginning, aka. »What's Inside«.
- Investigate subsystems of dbt Core, and unlock more of them by working through
  existing test cases of dbt-postgres which are currently being skipped. Maybe a
  few of them can be unlocked by applying corresponding workarounds/polyfills
  for CrateDB.
- [dbt-cratedb:/macros] might also include more gems that want to be absorbed by
  `dbt-cratedb2`, in order to provide a canonical package to the community.
  Let's also inform its authors afterwards.
- Scan the [genesis patch] for relevant TODO and FIXME items, to converge
  them into upstream tickets at `dbt`, or downstream at `crate/crate`

## Iteration +3
- Feature capabilities aim to be expanded and interoperability wants to be probed,
  [Interoperability with dbt ecosystem].
- Testing: From `release-internal.yml` GHA workflow.
  ```shell
  python -c "import dbt.adapters.cratedb"
  ```
  - https://docs.getdbt.com/docs/build/data-tests
  - https://docs.getdbt.com/reference/node-selection/test-selection-examples
- Use psycopg3?

## Done
- Fix missing `REFRESH TABLE`
  https://github.com/crate/dbt-cratedb2/issues/17


[CrateDB and dbt documentation page]: https://cratedb.com/docs/guide/integrate/dbt/
[dbt-cratedb:/macros]: https://github.com/crate-workbench/dbt-cratedb/tree/main/dbt/include/cratedbadapter/macros
[genesis patch]: https://github.com/crate-workbench/dbt-cratedb2/pull/2
[Interoperability with dbt ecosystem]: https://github.com/crate/dbt-cratedb2/discussions/18
[trusted adapter]: https://docs-getdbt-com-git-fork-crate-workbench-cratedb-dbt-labs.vercel.app/docs/trusted-adapters
[What it means to be trusted]: https://docs-getdbt-com-git-fork-crate-workbench-cratedb-dbt-labs.vercel.app/guides/adapter-creation#what-it-means-to-be-trusted
