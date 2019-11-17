# 在命令行执行python3 lesson5.py
# curl http://localhost:8080/page/1
from flask import Flask,jsonify
import pymysql
app = Flask(__name__)

# 配置复制上一个教程
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='blog',
    charset='utf8' 
)

@app.route('/page/<index>', methods=['GET'])
def page(index):
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 字符串拼接的方式不安全,于是官方库可以用下面的方式自动填入
    sql = '''select * from page where `index`=%s'''

    # args中的元素,会逐一替代上面的%s
    args = (index,)

    cursor.execute(sql,args)

    row = cursor.fetchone()

    # 现在,我们的返回值是json类型的了
    return jsonify(row)

app.run(debug=True, host='0.0.0.0', port=8080)