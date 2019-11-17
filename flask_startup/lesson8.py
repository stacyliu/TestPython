from flask import Flask,jsonify,request,redirect,url_for
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
    cursor.close()
    title = row.get('title')
    content = row.get('content')
    # 返回一个博文页面
    return '<div>'+ title +'</div><div>'+content+'</div>'

@app.route('/pages', methods=['GET'])
def pages():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = '''select * from page'''
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    
    # 返回一组博文的页面
    res = ''
    for row in rows:
        title = row.get('title')
        content = row.get('content')
        res = res + '<div>'+title+'</div><div>'+content+'</div>'
    return res

@app.route('/write', methods=['post'])
def write():
    title = request.form.get('title')
    content = request.form.get('content')
    cursor = conn.cursor()
    sql = '''insert into page (title, content) values (%s,%s)'''
    cursor.execute(sql,(title,content,))
    conn.commit()
    cursor.close()
    return 'done'

@app.route('/write', methods=['get'])
def writeHtml():
    # 返回一个form,用于写博文
    return '''<form action="/write" method="post">
                <input name="title" />
                <input name="content" />
                <button type="submit">发布</button>
              </form>'''

app.run(debug=True, host='0.0.0.0', port=8080)