<p align="center">
  <img src="https://raw.githubusercontent.com/dbt-labs/dbt/ec7dee39f793aa4f7dd3dae37282cc87664813e4/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
</p>
<p align="center">
  <a href="https://github.com/crate-workbench/dbt-cratedb2/actions/workflows/unit-tests.yml">
    <img src="https://github.com/crate-workbench/dbt-cratedb2/actions/workflows/unit-tests.yml/badge.svg?event=push" alt="CI Badge » Unit Tests"/>
  </a>
  <a href="https://github.com/crate-workbench/dbt-cratedb2/actions/workflows/integration-tests.yml">
    <img src="https://github.com/crate-workbench/dbt-cratedb2/actions/workflows/integration-tests.yml/badge.svg?event=push" alt="CI Badge » Integration Tests"/>
  </a>
</p>

## dbt-cratedb2

The `dbt-cratedb2` package contains all the code enabling [dbt] to work with a
[CrateDB] database.

Because CrateDB is PostgreSQL-compatible, dbt-cratedb2
heavily builds upon the canonical [dbt-postgres] adapter.
For more information on using dbt with CrateDB,
consult [the docs](https://docs.getdbt.com/docs/profile-cratedb).

## About dbt

dbt enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

## Getting started

- [Install dbt](https://docs.getdbt.com/docs/installation)
- Read the [introduction](https://docs.getdbt.com/docs/introduction/) and [viewpoint](https://docs.getdbt.com/docs/about/viewpoint/)

## Installation
Install dbt-cratedb2.
```shell
pip install 'dbt-cratedb2 @ git+https://github.com/crate-workbench/dbt-cratedb2.git'
```

### `psycopg2-binary` vs. `psycopg2`

By default, `dbt-cratedb2` installs `psycopg2-binary`. This is great for development, and even testing, as it does not require any OS dependencies; it's a pre-built wheel. However, building `psycopg2` from source will grant performance improvements that are desired in a production environment. In order to install `psycopg2`, use the following steps:

```bash
if [[ $(pip show psycopg2-binary) ]]; then
    PSYCOPG2_VERSION=$(pip show psycopg2-binary | grep Version | cut -d " " -f 2)
    pip uninstall -y psycopg2-binary
    pip install psycopg2==$PSYCOPG2_VERSION
fi
```

This ensures the version of `psycopg2` will match that of `psycopg2-binary`.


## Contribute

- Want to report a bug or request a feature? Let us know by [opening an issue](https://github.com/crate-workbench/dbt-cratedb2/issues/new)
- Want to help us build dbt-cratedb2? Check out the [contributing guide](https://github.com/crate-workbench/dbt-cratedb2/blob/main/CONTRIBUTING.md)
- Join the community on the [CrateDB Community Discourse](https://community.cratedb.com/)

## Code of Conduct

Everyone interacting with Crate.io's codebases, issue trackers, chat rooms, and mailing lists, please follow the [CrateDB Code of Conduct](https://github.com/crate/crate/blob/master/CODE_OF_CONDUCT.md).


[CrateDB]: https://github.com/crate/crate
[dbt]: https://www.getdbt.com/
[dbt-postgres]: https://github.com/dbt-labs/dbt-postgres
