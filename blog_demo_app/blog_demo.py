from flask import Flask
from flask_script import Manager, Server
from blog_demo_app.view_artical_pages import blueprint_pages
from blog_demo_app.view_login_and_register import blueprint_login

app = Flask(__name__)
app.secret_key = b'fghjkjhgvfcvhjkl/'
app.register_blueprint(blueprint=blueprint_login)
app.register_blueprint(blueprint=blueprint_pages)
manager=Manager(app=app)
manager.add_command("runserver", Server(use_debugger=True))

if __name__ == '__main__':
    manager.run()