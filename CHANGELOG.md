# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased
- Tests: Added integration test case with CrateDB using `rename_relation`
- Macro: Added `cratedb__reset_csv_table` for using `DELETE FROM`
  instead of `TRUNCATE`. Thanks, @hlcianfagna.
- Dependencies: Updated to `dbt-postgres>=1.9.0`

## v0.0.2 - November 26, 2024
- Maintenance release after migrating project and updating docs

## v0.0.1 - November 26, 2024
- Friendly fork from dbt-postgres 1.9.0-b1 - September 25, 2024
