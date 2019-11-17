from flask import Flask
from flask_script import Manager

from flask_lesson.view_new_blueprint import index_blueprint

app = Flask(__name__)
app.register_blueprint(blueprint=index_blueprint)
manager=Manager(app=app,)

if __name__ == '__main__':
    manager.run()