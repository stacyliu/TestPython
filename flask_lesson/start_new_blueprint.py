from flask import Flask
from flask_script import Manager, Server

from flask_lesson.view_new_blueprint import index_blueprint

app = Flask(__name__)
app.register_blueprint(blueprint=index_blueprint)
manager=Manager(app=app)
manager.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
    manager.run()