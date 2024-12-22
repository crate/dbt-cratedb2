# dbt-cratedb2 sandbox

## Setup
```shell
uv venv
source .venv/bin/activate
uv pip install hatch
```

## Usage
Start CrateDB.
```shell
docker run --rm -it --name=cratedb \
  --publish=4200:4200 --publish=5432:5432 \
  --env=CRATE_HEAP_SIZE=8g crate/crate:nightly \
  -Ccluster.max_shards_per_node=5000 \
  -Cdiscovery.type=single-node
```
Invoke software tests.
```shell
hatch run unit-tests
hatch run integration-tests
```

## Release
- Bump version in `dbt/adapters/cratedb/__version__.py`.
- Edit `CHANGELOG.md`, designating a new release.
- Repository: Tag and Push.
  ```shell
  git commit -m "Release v0.1.0"
  git tag v0.1.0
  git push && git push --tags
  ```
- PyPI: Build and publish
  ```shell
  hatch build
  hatch publish
  ```
- GitHub: Designate new release.
  https://github.com/crate/dbt-cratedb2/releases
