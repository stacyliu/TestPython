from flask import Flask
from flask_script import Manager
from flask_lesson.view import a
#循环引用


app = Flask(__name__)
manager=Manager(app=app)
print(a)

if __name__ == '__main__':
    manager.run()