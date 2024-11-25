{# CrateDB: `pg_rewrite` not implemented #}
{# TODO: Use original `postgres__get_relations` #}
{% macro cratedb__get_relations() -%}
  {%- call statement('relations', fetch_result=True) -%}
    {# FIXME: Is that mock enough to satisfy expectations? #}
    select 'mock' as referenced_schema,
           'referenced' as referenced_name,
           'mock' as dependent_schema,
           'dependent' as dependent_name;
  {%- endcall -%}

  {{ return(load_result('relations').table) }}
{% endmacro %}

{# TODO: Needs a software test #}
{% macro cratedb__list_relations_without_caching(schema_relation) %}
  {% call statement('list_relations_without_caching', fetch_result=True) -%}
    select
      '{{ schema_relation.database }}' as database,
      tablename as name,
      schemaname as schema,
      'table' as type
    from pg_tables
    where schemaname ilike '{{ schema_relation.schema }}'
    union all
    select
      '{{ schema_relation.database }}' as database,
      viewname as name,
      schemaname as schema,
      'view' as type
    from pg_views
    where schemaname ilike '{{ schema_relation.schema }}'
    {# CrateDB: MATERIALIZED VIEW not supported #}
    {#
    union all
    select
      '{{ schema_relation.database }}' as database,
      matviewname as name,
      schemaname as schema,
      'materialized_view' as type
    from pg_matviews
    where schemaname ilike '{{ schema_relation.schema }}'
    #}
  {% endcall %}
  {{ return(load_result('list_relations_without_caching').table) }}
{% endmacro %}
