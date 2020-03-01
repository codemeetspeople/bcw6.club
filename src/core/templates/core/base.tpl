<html>
    <!DOCTYPE html>
    <head>
        <meta charset="utf-8">
        <title>{% block title %}Home{% endblock %}</title>
    </head>
    <body> 
        {% block content %}
        <h1>Hello, Django!</h1>
        {% endblock %}
    </body>
</html>