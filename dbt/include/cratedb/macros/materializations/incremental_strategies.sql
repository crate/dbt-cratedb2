{% macro cratedb__get_incremental_default_sql(arg_dict) %}

  {% if arg_dict["unique_key"] %}
    {% do return(get_incremental_delete_insert_sql(arg_dict)) %}
  {% else %}
    {% do return(get_incremental_append_sql(arg_dict)) %}
  {% endif %}

{% endmacro %}


{% macro cratedb__get_incremental_microbatch_sql(arg_dict) %}

  {% if arg_dict["unique_key"] %}
    {% do return(adapter.dispatch('get_incremental_merge_sql', 'dbt')(arg_dict)) %}
  {% else %}
    {{ exceptions.raise_compiler_error("dbt-cratedb2 'microbatch' requires a `unique_key` config") }}
  {% endif %}

{% endmacro %}
