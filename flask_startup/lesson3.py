# 在命令行执行python3 lesson3.py
# curl http://localhost:8080/page/3
from flask import Flask
app = Flask(__name__)

# curl http://localhost:8080/page/3
# 下面一行是指定url,url是可变的,比如3可以换成任意数字
@app.route('/page/<index>', methods=['GET'])

# 上面用尖括号把index包起来后,下面就可以用index变量了
# 但是注意,要把index变量传递进去
def page(index):
    # index变量是字符串类型的,使用时需要转换成数字
    index = int(index)

    # 返回时需要转换成字符串类型
    return 'now page is ' + str(index)

# 这里监听换成0.0.0.0,以前只能通过localhost进行访问,现在可以通过ip进行访问
app.run(debug=True, host='0.0.0.0', port=8080)