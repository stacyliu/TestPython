from flask import Flask,jsonify,request,redirect,url_for
import pymysql
app = Flask(__name__)

# 配置复制上一个教程
conn = pymysql.connect(
    host='localhost',
    user='root',
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
    
    # 用格式化字符串写法
    return '<div>%s</div><div>%s</div>' % (title,content,)

@app.route('/pages', methods=['GET'])
def pages():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = '''select * from page'''
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    
    # 增加跳转到单页的特性
    res = ''
    for row in rows:
        title = row.get('title')
        content = row.get('content')
        index = row.get('index')
        res = res + '<div><a href="/page/%d">%s</a></div><div>%s</div>' % (index,title,content,)
    return res

@app.route('/write', methods=['post'])
def write():
    title = request.form.get('title')
    content = request.form.get('content')
    cursor = conn.cursor()
    sql = '''insert into page (title, content) values (%s,%s)'''
    # 数据库字符集可能有问题
    # ALTER TABLE page CHANGE content content text CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL;
    # ALTER TABLE page CHANGE title title text CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL;
    cursor.execute(sql,(title,content,))
    conn.commit()
    cursor.close()
    # 跳转到pages页面
    return redirect(url_for('pages'))

@app.route('/write', methods=['get'])
def writeHtml():
    # 美化页面
    return '''<form action="/write" method="post">
              标题<div><input name="title" /></div>
              内容<div><textarea name="content" cols="80" rows="10"></textarea></div>
              <div><button type="submit">发布</button></div>
              </form>
              <script>
                alert('1')
              </script>
              '''

app.run(debug=True, host='0.0.0.0', port=8080)