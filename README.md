<p align="center">
  <img src="https://raw.githubusercontent.com/dbt-labs/dbt/ec7dee39f793aa4f7dd3dae37282cc87664813e4/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
  <br/><br/>
  <img src="https://github.com/user-attachments/assets/70485bb9-9809-46ce-a189-858676780b2b" alt="dbt logo" width="500"/>
</p>
<p align="center">
  <a href="https://github.com/crate/dbt-cratedb2/actions/workflows/unit-tests.yml">
    <img src="https://github.com/crate/dbt-cratedb2/actions/workflows/unit-tests.yml/badge.svg?event=push" alt="CI Badge » Unit Tests"/>
  </a>
  <a href="https://github.com/crate/dbt-cratedb2/actions/workflows/integration-tests.yml">
    <img src="https://github.com/crate/dbt-cratedb2/actions/workflows/integration-tests.yml/badge.svg?event=push" alt="CI Badge » Integration Tests"/>
  </a>
</p>

## dbt-cratedb2

The `dbt-cratedb2` package contains all the code enabling [dbt] to work with a
[CrateDB] database.

CrateDB is PostgreSQL-compatible, that's why dbt-cratedb2
heavily builds upon the canonical [dbt-postgres] adapter.
For more information on using dbt with CrateDB,
consult [the docs].

## About dbt

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

## About CrateDB

CrateDB is a distributed and scalable SQL database for storing and analyzing
massive amounts of data in near real-time, even with complex queries.
It is PostgreSQL-compatible, and based on Lucene.

## Getting started

- [Install dbt](https://docs.getdbt.com/docs/core/installation-overview)
- Read the [introduction](https://docs.getdbt.com/docs/introduction/) and
  [viewpoint](https://docs.getdbt.com/community/resources/viewpoint)

## Installation
Install dbt-cratedb2.
```shell
pip install --upgrade 'dbt-cratedb2'
```

## `psycopg2`
By default, `dbt-cratedb2` installs `psycopg2-binary`.
For more information, please visit [psycopg2 notes].

## Contribute

- Want to report a bug or request a feature? Let us know by [opening an issue]
- Want to help us build dbt-cratedb2? Check out the [contributing guide]
- Join the community on the [CrateDB Community Discourse]

## Code of Conduct

Everyone interacting with Crate.io's codebases, issue trackers, chat rooms, and mailing lists, please follow the [CrateDB Code of Conduct].


[contributing guide]: https://github.com/crate/dbt-cratedb2/blob/main/CONTRIBUTING.md
[CrateDB]: https://github.com/crate/crate
[CrateDB Code of Conduct]: https://github.com/crate/crate/blob/master/CODE_OF_CONDUCT.md
[CrateDB Community Discourse]: https://community.cratedb.com/
[dbt]: https://www.getdbt.com/
[dbt-postgres]: https://github.com/dbt-labs/dbt-postgres
[opening an issue]: https://github.com/crate/dbt-cratedb2/issues/new
[psycopg2 notes]: https://github.com/crate/dbt-cratedb2/blob/genesis/docs/psycopg2.md
[the docs]: https://docs.getdbt.com/docs/core/connect-data-platform/cratedb-setup
