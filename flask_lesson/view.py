import manage

from manage import app

a=10
@app.route('/')
def hello_world():
    return 'hello_world'