# Part 02

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

### Make app/templates
```shell
(venv) $ mkdir app/templates
```

### Create app/templates/index.html: Main page template
```html
<!doctype html>
<html>
    <head>
        <title>{{ title }} - Microblog</title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>
```

### Configuration of routes.py
1. We can concatenate data into our returned html string
2. We can return a rendered template, which can inject data from routes.py

### Configuration of templates
1. We can use conditional statements using {% if %}, {% else %}, {% endif %}  syntax
2. We can loop using {% for item in items %} {% endfor %}
3. We can inherit from a base template using {% block content %} {% endblock %} and {% extends "base.html" %}