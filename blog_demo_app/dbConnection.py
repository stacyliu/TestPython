import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    database='blog',
    charset='utf8'
)