# psycopg2 notes

A few notes about `psycopg2-binary` vs. `psycopg2`.

By default, `dbt-cratedb2` installs `psycopg2-binary`. This is great for development,
and even testing, as it does not require any OS dependencies; it's a pre-built wheel.
However, building `psycopg2` from source will grant performance improvements that are
desired in a production environment. In order to install `psycopg2`, use the
following steps:

```bash
if [[ $(pip show psycopg2-binary) ]]; then
    PSYCOPG2_VERSION=$(pip show psycopg2-binary | grep Version | cut -d " " -f 2)
    pip uninstall -y psycopg2-binary
    pip install psycopg2==$PSYCOPG2_VERSION
fi
```

This ensures the version of `psycopg2` will match that of `psycopg2-binary`.
