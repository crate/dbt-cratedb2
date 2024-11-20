{% macro get_create_table_as_sql(temporary, relation, sql) -%}
  {{ adapter.dispatch('get_create_table_as_sql', 'cratedb')(False, relation, sql) }}
{%- endmacro %}

{% macro cratedb__get_create_table_as_sql(temporary, relation, sql) -%}
  {{ return(cratedb__create_table_as(False, relation, sql)) }}
{% endmacro %}

{% macro default__get_create_table_as_sql(temporary, relation, sql) -%}
  {{ return(cratedb__create_table_as(False, relation, sql)) }}
{% endmacro %}


{# Needs an override because CrateDB does not support `CREATE TEMPORARY TABLE` #}
{% macro cratedb__create_table_as(temporary, relation, sql) -%}
  {%- set unlogged = config.get('unlogged', default=false) -%}
  {%- set sql_header = config.get('sql_header', none) -%}

  {{ sql_header if sql_header is not none }}

  create {% if temporary -%}
  {%- elif unlogged -%}
    unlogged
  {%- endif %} table {{ relation }}
  {% set contract_config = config.get('contract') %}
  {% if contract_config.enforced %}
    {{ get_assert_columns_equivalent(sql) }}
  {% endif -%}
  {% if contract_config.enforced and (not temporary) -%}
      {{ get_table_columns_and_constraints() }} ;
    insert into {{ relation }} (
      {{ adapter.dispatch('get_column_names', 'dbt')() }}
    )
    {%- set sql = get_select_subquery(sql) %}
  {% else %}
    as
  {% endif %}
  (
    {{ sql }}
  );
{%- endmacro %}

{% macro cratedb__create_schema(relation) -%}
  {% if relation.database -%}
    {{ adapter.verify_database(relation.database) }}
  {%- endif -%}
  {%- call statement('create_schema') -%}
  {# create schema if not exists {{ relation.without_identifier().include(database=False) }} #}
    SELECT 1
  {%- endcall -%}
{% endmacro %}

{% macro cratedb__drop_schema(relation) -%}
  {% if relation.database -%}
    {{ adapter.verify_database(relation.database) }}
  {%- endif -%}
  {%- call statement('drop_schema') -%}
  {# drop schema if exists {{ relation.without_identifier().include(database=False) }} cascade #}
    SELECT 1
  {%- endcall -%}
{% endmacro %}
