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

{% endmacro %}
