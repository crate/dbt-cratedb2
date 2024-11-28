{# CrateDB: Use `DELETE FROM` instead of `TRUNCATE` #}
{% macro cratedb__reset_csv_table(model, full_refresh, old_relation, agate_table) %}
    {% set sql = "" %}
    {% if full_refresh %}
        {{ adapter.drop_relation(old_relation) }}
        {% set sql = create_csv_table(model, agate_table) %}
    {% else %}
        {{ adapter.truncate_relation(old_relation) }}
        {% set sql = "delete from " ~ old_relation.render() %}
    {% endif %}

    {{ return(sql) }}
{% endmacro %}
