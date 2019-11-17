# 先执行pip3 install pymysql

# docker启动mysql docker run -d --name sql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root mysql:5.6
# 在命令行执行python3 lesson4.py
# curl http://localhost:8080/page/1
from flask import Flask
app = Flask(__name__)

# 引入连接mysql的库
import pymysql

# 配置数据库连接方式,并且连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='blog',
    charset='utf8' 
)

@app.route('/page/<index>', methods=['GET'])
def page(index):

    # 创建数据库光标,必须使用cursor才能调用sql语句
    # 数据库规定这么使用的,没有为什么.
    # 后面参数的意思是返回类型改成hashmap
    # 如果不加参数,返回类型是数组
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 定义要执行的SQL语句,根据你的表结构进行修改
    sql = '''select * from page where `index`=''' + index

    # 执行SQL语句
    cursor.execute(sql)
  
    # 获取所有结果
    row = cursor.fetchone()
    # 返回的样子是这样的{ "title":"testTitle","content":"testContent","index":1}

    # 获取标题和内容
    title = row.get("title")
    content = row.get("content")

    return 'title is ' + title + '. content is ' + content

app.run(debug=True, host='0.0.0.0', port=8080)