{% macro cratedb__drop_view(relation) -%}
    drop view if exists {{ relation }}
{%- endmacro %}
