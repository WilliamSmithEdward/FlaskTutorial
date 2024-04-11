from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello, World!</h1><h3>My name is William Smith</h3>"