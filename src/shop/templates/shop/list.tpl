{% extends 'core/base.tpl' %}

{% block title %}Categories{% endblock %}

{% block content %}
    <br />
    {% for object in objects %}
        <div>
            <center>
                <h1>
                    {% set url_name = 'shop:' + route %}
                    <a href="{{ url(url_name, object.id) }}">{{ object.title }}</a>
                </h1>
            </center>
        </div>
        <hr />
        <br />
    {% endfor %}
{% endblock %}