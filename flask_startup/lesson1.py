# 先执行pip3 install Flask
# 在命令行执行python3 lesson1.py
# 再打开一个窗口 curl http://localhost:8080/hello
# ctrl-c 停止运行

# 引入flask库

from flask import Flask
from flask_script import *


# 初始化flask对象
app = Flask(__name__)
manager=Manager(app=app)

# 装饰器,指明访问路径.执行命令行 curl http://localhost:8080/hello 可返回结果
@app.route('/hello')

# 随便起一个方法名,名字随意起,但不能重名
def hello_world():
    # 设置服务器返回值
    return 'Hello, World!'

# 启动服务器,指定监听8080端口
if __name__ == '__main__':
    manager.run()