{% macro cratedb__drop_table(relation) -%}
    drop table if exists {{ relation }}
{%- endmacro %}
