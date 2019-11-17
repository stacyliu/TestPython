from flask import Flask, render_template
from flask_script import *


# 初始化flask对象
app = Flask(__name__)
manager=Manager(app=app)

# 装饰器,指明访问路径.执行命令行 curl http://localhost:8080/hello 可返回结果
@app.route('/')
# 随便起一个方法名,名字随意起,但不能重名
def hello_world():
    # 设置服务器返回值
    return render_template("/index.html")

#html 创建一个templates文件夹 放在里面
#js 创建一个static文件夹 放在里面
# 启动服务器,指定监听8080端口
if __name__ == '__main__':
    manager.run(debug=True)