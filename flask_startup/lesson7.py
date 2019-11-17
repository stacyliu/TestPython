from flask import Flask,jsonify,request
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
    # 数据库游标需要手动关闭,养成关闭的好习惯
    cursor.close()
    return jsonify(row)

@app.route('/pages', methods=['GET'])
def pages():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = '''select * from page'''
    cursor.execute(sql)
    row = cursor.fetchall()
    # 数据库游标需要手动关闭,养成关闭的好习惯
    cursor.close()
    return jsonify(row)

# curl -d "title=testTitle&content=testContent" -X post http://localhost:8080/write
@app.route('/write', methods=['post'])
def login():
    # 网页使用form上传,后端获取form
    title = request.form.get('title')
    content = request.form.get('content')

    cursor = conn.cursor()
    sql = '''insert into page (title, content) values (%s,%s)'''
    cursor.execute(sql,(title,content,))

    #增删改需要进行数据库的commit提交
    conn.commit()
    cursor.close()
    return "done"

app.run(debug=True, host='0.0.0.0', port=8080)