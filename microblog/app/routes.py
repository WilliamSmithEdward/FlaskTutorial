from flask import render_template
from app import app

@app.route('/')
def index():
    return render_template('index_00.html', title='Home')

@app.route('/index_helloworld')
def index_helloworld():
    user = {'username': 'William'}
    return render_template('index_01_helloworld.html', title='Home', user=user)

@app.route('/index_conditionals')
def index_conditionals():
    user = {'username': 'William'}
    return render_template('index_02_conditionals.html', title='Home', user=user)

@app.route('/index_loops')
def index_loops():
    user = {'username': 'William'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index_03_loops.html', title='Home', user=user, posts=posts)

@app.route('/index_inheritance')
def index_inheritance():
    user = {'username': 'William'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index_04_inheritance_B.html', title='Home', user=user, posts=posts)