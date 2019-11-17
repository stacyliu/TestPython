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
    sql = '''select * from page where `index`=%s'''
    args = (index,)
    cursor.execute(sql,args)
    row = cursor.fetchone()
    return jsonify(row)

@app.route('/pages', methods=['GET'])
def pages():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = '''select * from page'''
    cursor.execute(sql)
    row = cursor.fetchall()
    return jsonify(row)

app.run(debug=True, host='0.0.0.0', port=8080)