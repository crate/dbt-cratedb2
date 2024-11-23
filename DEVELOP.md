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
