from flask import Flask, render_template
from flask_script import *

# 初始化flask对象
app = Flask(__name__)
manager=Manager(app=app)
@app.route('/')
def hello_world():
    # 设置服务器返回值
    a={"b":"111","c":"222"}
    rows=[{"id":"1","content":"c1","title":"t1","readCount":"r1"},{"id":"2","content":"c2","title":"t2","readCount":"r2"}]
    s=render_template("/pages_title.html")
    for row in rows:
         s=s+render_template("/pages.html",artical=row)
    return s

#html 创建一个templates文件夹 放在里面
#js 创建一个static文件夹 放在里面
# 启动服务器,指定监听8080端口
if __name__ == '__main__':
    manager.run(debug=True)