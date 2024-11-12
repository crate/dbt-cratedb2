# Contributing to `dbt-cratedb2`

- [About this document](#about-this-document)
- [Getting the code](#getting-the-code)
- [Developing](#developing)
- [Testing](#testing)
- [Documentation](#documentation)
- [Submitting a pull request](#submitting-a-pull-request)


## About this document

This document is a guide for anyone interested in contributing to `dbt-cratedb2`.
It outlines how to install `dbt-cratedb2` for development,
run tests locally, update documentation, and submit pull requests.
This guide assumes users are developing on a Linux or MacOS system.
The following utilities are needed or will be installed in this guide:

- `pip`
- `virturalenv`
- `git`

If local functional testing is required, then a database instance
and appropriate credentials are also required.

In addition to this guide, users are highly encouraged to read the [CrateDB
contribution guidelines](https://github.com/crate/crate/blob/master/CONTRIBUTING.rst).
Almost all information there is also applicable here.


## Getting the code

`git` is required to download, modify, and sync the `dbt-cratedb2` code.
There are several ways to install Git. For MacOS:

- Install [Xcode](https://developer.apple.com/support/xcode/)
- Install [Xcode Command Line Tools](https://mac.install.guide/commandlinetools/index.html)

### External contributors

Contributors external to the `crate` GitHub organization can contribute to `dbt-cratedb2`
by forking the `dbt-cratedb2` repository. For more on forking, check out the
[GitHub docs on forking](https://help.github.com/en/articles/fork-a-repo). To contribute:

1. Fork the `crate-workbench/dbt-cratedb2` repository (e.g. `{forked-org}/dbt-cratedb2`)
2. Clone `{forked-org}/dbt-cratedb2` locally
3. Check out a new branch locally
4. Make changes in the new branch
5. Push the new branch to `{forked-org}/dbt-cratedb2`
6. Open a pull request in `crate-workbench/dbt-cratedb2` to merge `{forked-org}/dbt-cratedb2/{new-branch}` into `main`

### CrateDB contributors

Contributors in the `crate` GitHub organization have push access to the `dbt-cratedb2` repo.
Rather than forking `crate-workbench/dbt-cratedb2`, use `crate-workbench/dbt-cratedb2` directly. To contribute:

1. Clone `crate-workbench/dbt-cratedb2` locally
2. Check out a new branch locally
3. Make changes in the new branch
4. Push the new branch to `crate-workbench/dbt-cratedb2`
5. Open a pull request in `crate-workbench/dbt-cratedb2` to merge `{new-branch}` into `main`


## Developing

### Installation

1. Ensure the latest versions of `pip` and `hatch` are installed:
   ```shell
   pip install --user --upgrade pip hatch
   ```
2. This step is optional, but it's recommended. Configure `hatch` to create its virtual environments in the project. Add this block to your `hatch` `config.toml` file:
   ```toml
   # MacOS: ~/Library/Application Support/hatch/config.toml
   [dirs.env]
   virtual = ".hatch"
   ```
   This makes `hatch` create all virtual environments in the project root inside of the directory `/.hatch`, similar to `/.tox` for `tox`.
   It also makes it easier to add this environment as a runner in common IDEs like VSCode and PyCharm.
3. Create a `hatch` environment with all of the development dependencies and activate it:
   ```shell
   hatch run setup
   hatch shell
   ```
4. Run any commands within the virtual environment by prefixing the command with `hatch run`:
   ```shell
   hatch run <command>
   ```

When `dbt-cratedb2` is installed this way, any changes made to the `dbt-cratedb2` source code
will be reflected in the virtual environment immediately.

## Testing

`dbt-cratedb2` contains [code quality checks](https://github.com/crate-workbench/dbt-cratedb2/tree/main/.pre-commit-config.yaml), [unit tests](https://github.com/crate-workbench/dbt-cratedb2/tree/main/tests/unit),
and [functional tests](https://github.com/crate-workbench/dbt-cratedb2/tree/main/tests/functional).

### Code quality

Code quality checks can run with a single command:
```shell
hatch run code-quality
```

### Unit tests

Unit tests can be run locally without setting up a database connection:

```shell
# Note: replace $strings with valid names

# run all unit tests
hatch run unit-test

# run all unit tests in a module
hatch run unit-tests tests/unit/$test_file_name.py

# run a specific unit test
hatch run unit-tests tests/unit/$test_file_name.py::$test_class_name::$test_method_name
```

### Functional tests

Functional tests require a database to test against. There are two primary ways to run functional tests:

- Tests on CI will run automatically against a configured database during PR checks
- Tests can be run locally by configuring a `test.env` file with appropriate `ENV` variables:
   ```shell
   cp test.env.example test.env
   $EDITOR test.env
   ```

> **_WARNING:_** The parameters in `test.env` must link to a valid database.
> `test.env` is git-ignored, but be _extra_ careful to never check in credentials
> or other sensitive information when developing.

Functional tests can be run locally with a valid database connection configured in `test.env`:

```shell
# Note: replace $strings with valid names

# run all functional tests
hatch run integration-tests

# run all functional tests in a directory
hatch run integration-tests tests/functional/$test_directory

# run all functional tests in a module
hatch run integration-tests tests/functional/$test_directory/$test_filename.py

# run all functional tests in a class
hatch run integration-tests tests/functional/$test_directory/$test_filename.py::$test_class_name

# run a specific functional test
hatch run integration-tests tests/functional/$test_directory/$test_filename.py::$test_class_name::$test__method_name
```

### Testing against a development branch

Some changes require a change in `dbt-common` and/or `dbt-adapters`.
In that case, the dependency on `dbt-common` and/or `dbt-adapters` must be updated to point to the development branch. For example:

```toml
[tool.hatch.envs.default]
dependencies = [
    "dbt-common @ git+https://github.com/dbt-labs/dbt-common.git@my-dev-branch",
    "dbt-adapters @ git+https://github.com/dbt-labs/dbt-adapters.git@my-dev-branch",
    "dbt-tests-adapter @ git+https://github.com/dbt-labs/dbt-adapters.git@my-dev-branch#subdirectory=dbt-tests-adapter",
    ...,
]
```

This will install `dbt-common`/`dbt-adapters`/`dbt-tests-adapter` as snapshots. In other words, if `my-dev-branch` is updated on GitHub, those updates will not be reflected locally.
In order to pick up those updates, the `hatch` environment(s) will need to be rebuilt:

```shell
exit
hatch env prune
hatch shell
```

## Documentation

### User documentation

Many changes will require an update to `dbt-cratedb2` user documentation
within the `docs/` folder in this repository. Please make sure your patches
are complete by including relevant updates.


## Submitting a pull request

### Signing the CLA

> **_NOTE:_** All contributors to `dbt-cratedb2` must sign the
> [Contributor License Agreement](https://cratedb.com/developers/community/contribute)(CLA).

Maintainers will be unable to merge contributions until the contributor signs the CLA.
This is a one time requirement, not a per-PR requirement.
Even without a CLA, anyone is welcome to open issues and comment on existing issues or PRs.

### Opening a pull request

A `dbt-cratedb2` maintainer will be assigned to review each PR based on priority and capacity.
They may suggest code revisions for style and clarity or they may request additional tests.
These are good things! Crate.io believes that contributing high-quality code is a collaborative effort.
The same process is followed whether the contributor is external or another `dbt-cratedb2` maintainer.
Once all tests are passing and the PR has been approved by the appropriate code owners,
a `dbt-cratedb2` maintainer will merge the changes into `main`.

And that's it! Happy developing :tada:
