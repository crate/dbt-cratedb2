{#- /*Postgres doesn't support any_value, so we're using min() to get the same result*/ -#}

{% macro cratedb__any_value(expression) -%}

    min({{ expression }})

{%- endmacro %}
