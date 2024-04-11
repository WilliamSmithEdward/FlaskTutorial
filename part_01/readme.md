# Part 01

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

### Create microblog directory
```shell
$ mkdir microblog
$ cd microblog
```

### Establish python virtual environment (venv) 
```shell
# OSX may require python3.12
$ python3 -m venv venv
```
https://docs.python.org/3/library/venv.html

Note: When activating the venv in OSX VS Code, I had trouble selecting the proper interpreter in the venv. I used the following steps to resolve:

1. COMMAND + SHIFT + P
2. Python: Select Interpreter
3. Enter interpreter path...
4. Type in the path to the venv ~/documents/GitHub/FlaskTutorial/part_01/microblog/venv/bin/python

Browsing for the interpreter did not work.

### Activate venv
```shell
# *nix
$ source venv/bin/activate
# Windows Terminal
$ source venv/bin/activate
# Windows PowerShell
$ venv\Scripts\Activate.ps1
```

### Install flask into venv
```shell
(venv) $ pip install flask
```

### Make app directory 
```shell
(venv) $ mkdir app
(venv) $ cd app
```

### Create app/\_\_init\_\_.py: Flask application instance
```python
from flask import Flask

app = Flask(__name__)

from app import routes
```

### Create app/routes.py: Home page route
```python
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
```

### Create microblog.py: Main application module
```python
from app import app
```

### Create .flaskenv: Environment variables for flask command
```python
FLASK_APP=microblog.py
```

### Run Flask
```shell
# Optional --debug flag will allow hot reloading of changes
flask run --debug
```