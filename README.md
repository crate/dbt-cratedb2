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

# dbt-cratedb2

[![Package version][badge-package-version]][project-pypi]
[![Release Notes][badge-release-notes]][project-release-notes]
[![Downloads per month][badge-downloads-per-month]][project-downloads]

[![License][badge-license]][project-license]
[![Status][badge-status]][project-pypi]
[![Supported Python versions][badge-python-versions]][project-pypi]

» [Documentation]
| [Changelog]
| [PyPI]
| [Issues]
| [Source code]
| [License]
| [CrateDB]
| [Community Forum]

The `dbt-cratedb2` package contains all the code enabling [dbt] to work with
[CrateDB Self-Managed] or [CrateDB Cloud].

**[dbt]** enables data analysts and engineers to transform their data using the
same practices that software engineers use to build applications.
dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and
pre-aggregate the raw data in your warehouse so that it's ready for analysis.

**[CrateDB]** is a distributed and scalable SQL database for storing and
analyzing massive amounts of data in near real-time, even with complex queries.
It is PostgreSQL-compatible, and based on Lucene.

## Installation
Install the most recent version of dbt-cratedb2.
```shell
pip install --upgrade dbt-cratedb2
```

## Getting started

- [Install dbt](https://docs.getdbt.com/docs/core/installation-overview).
- Read the dbt [introduction](https://docs.getdbt.com/docs/introduction/) and
  [viewpoint](https://docs.getdbt.com/community/resources/viewpoint).
- Read about how to [use dbt with CrateDB].

## What's Inside

CrateDB is PostgreSQL-compatible, that's why dbt-cratedb2
heavily builds upon the canonical [dbt-postgres] adapter.
For more information on using dbt with CrateDB,
consult [the docs].

### `psycopg2`
By default, `dbt-cratedb2` installs `psycopg2-binary`.
For more information, please visit [psycopg2 notes].


## Project Information

### Acknowledgements
Kudos to the authors of all the many software components this library is
inheriting from and building upon, most notably the [dbt-postgres]
package, and [dbt][dbt-core] itself.

### Contributing
The `dbt-cratedb2` package is an open source project, and is
[managed on GitHub]. We appreciate contributions of any kind.

- Want to report a bug or request a feature? Let us know by [opening an issue].
- Want to help us build dbt-cratedb2? Check out the [contributing guide].
- Join the community on the [CrateDB Community Discourse].

### License
The project uses the Apache Software License, like the dbt-postgres project
it is deriving from.

### Code of Conduct
Everyone interacting with Crate.io's codebases, issue trackers, chat rooms, and
mailing lists, please follow the [CrateDB Code of Conduct].


[contributing guide]: https://github.com/crate/dbt-cratedb2/blob/main/CONTRIBUTING.md
[CrateDB]: https://cratedb.com/database
[CrateDB Cloud]: https://cratedb.com/database/cloud
[CrateDB Self-Managed]: https://cratedb.com/database/self-managed
[CrateDB Code of Conduct]: https://github.com/crate/crate/blob/master/CODE_OF_CONDUCT.md
[CrateDB Community Discourse]: https://community.cratedb.com/
[dbt]: https://www.getdbt.com/
[dbt-core]: https://pypi.org/project/dbt-core/
[dbt-postgres]: https://pypi.org/project/dbt-postgres/
[opening an issue]: https://github.com/crate/dbt-cratedb2/issues/new
[psycopg2 notes]: https://github.com/crate/dbt-cratedb2/blob/genesis/docs/psycopg2.md
[the docs]: https://docs.getdbt.com/docs/core/connect-data-platform/cratedb-setup
[use dbt with CrateDB]: https://cratedb.com/docs/guide/integrate/dbt/

[Changelog]: https://github.com/crate/dbt-cratedb2/blob/main/CHANGELOG.md
[Community Forum]: https://community.cratedb.com/
[Documentation]: https://cratedb.com/docs/guide/integrate/dbt/
[Issues]: https://github.com/crate/dbt-cratedb2/issues
[License]: https://github.com/crate/dbt-cratedb2/blob/main/LICENSE
[managed on GitHub]: https://github.com/crate/dbt-cratedb2
[PyPI]: https://pypi.org/project/dbt-cratedb2/
[Source code]: https://github.com/crate/dbt-cratedb2

[badge-bluesky]: https://img.shields.io/badge/Bluesky-0285FF?logo=bluesky&logoColor=fff&label=Follow%20%40CrateDB
[badge-downloads-per-month]: https://pepy.tech/badge/dbt-cratedb2/month
[badge-license]: https://img.shields.io/github/license/crate/dbt-cratedb2.svg
[badge-package-version]: https://img.shields.io/pypi/v/dbt-cratedb2.svg
[badge-python-versions]: https://img.shields.io/pypi/pyversions/dbt-cratedb2.svg
[badge-release-notes]: https://img.shields.io/github/release/crate/dbt-cratedb2?label=Release+Notes
[badge-status]: https://img.shields.io/pypi/status/dbt-cratedb2.svg
[project-bluesky]: https://bsky.app/search?q=cratedb
[project-downloads]: https://pepy.tech/project/dbt-cratedb2/
[project-license]: https://github.com/crate/dbt-cratedb2/blob/main/LICENSE
[project-pypi]: https://pypi.org/project/dbt-cratedb2
[project-release-notes]: https://github.com/crate/dbt-cratedb2/releases
