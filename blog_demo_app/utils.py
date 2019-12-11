import pymysql
from flask import request, session, escape
from blog_demo_app.dbConnection import conn


class Utils:
    def isLoggedIn(self):
        if 'username' in session:
            return True
        else:
            return False


    def getUserName(self):
        if(self.isLoggedIn()):
            return session['username']
        else:
            return None
    #新用户往数据库写cookie-userid
    def setCookieOrGetCookie(self,cookie):
        if(cookie==None):
            #todo：设计表 列 存储什么值
            #该用户没有cookie 也就是从来没访问过这个网站
            #给他生成一个cookie存起来

            pass

    #登录用户数据库查询 通过cookie确认这个人是谁
    def getSessionFromCookie(self,cookie):
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #todo:设计表 列 存储什么值 返回字典/json应该也可以 在需要读cookie保持用户session时使用
        sql = '''select * from cookies where `cookie`=%s'''
        args = (cookie,)
        cursor.execute(sql, args)
        row = cursor.fetchone()
        #todo:返回值的数据类型
        dic={}
        dic.add("userid",row.getUserID())
        dic.add("userid", row.getUserID())

        cursor.close()
        return None;


