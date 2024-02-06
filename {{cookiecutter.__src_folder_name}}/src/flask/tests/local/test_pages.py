{# Template found in "templates" directory at root #}
{% if 'postgres' in cookiecutter.db_resource or 'mysql' in cookiecutter.db_resource %}
{% include "flask_test_pages_sql.py" %}
{% endif %}
{% if 'mongo' in cookiecutter.db_resource %}
{% include "flask_test_pages_mongodb.py" %}
{% endif %}