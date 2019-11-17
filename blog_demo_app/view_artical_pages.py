from flask import Blueprint
from flask import Flask, jsonify, request, redirect, url_for, render_template
import pymysql
from blog_demo_app.dbConnection import conn
import time
blueprint_pages=Blueprint("pages_blueprint",__name__)

@blueprint_pages.route('/page/<index>', methods=['GET'])
def page(index):
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = '''select * from artical where `id`=%s'''
    args = (index,)
    cursor.execute(sql, args)
    row = cursor.fetchone()

    title = row.get('title')
    content = row.get('content')
    likeCount=row.get('likeCount')
    createDate=row.get('createDate')
    readCount=row.get('readCount')
    print(likeCount,readCount,createDate)
    #没访问一次阅读数自加一次
    sql2 = 'update artical set `readCount`= %s WHERE `id`=%s'
    args2=(readCount+1,index)
    cursor.execute(sql2, args2)


    # 用格式化字符串写法
    resource=render_template("/page_main_artical.html", artical=row)
    #todo:获取当前文章的全部评论并且fetchall展示把输出写在resourceComment里

    sql3 = 'SELECT comment.userName, comment.commentContent FROM comment INNER JOIN artical ON comment.articalid=artical.id WHERE artical.id=%s ORDER BY comment.id;'
    args3 = (index)
    cursor.execute(sql3, args3)
    rows=cursor.fetchall()
    for row in rows:
        resource=resource+render_template("/page_comment.html",user=row)
    resource=resource+render_template("/page_send_comment.html",loginuser="123",articalIndex=index)
    conn.commit()
    cursor.close()
    return resource


#所有文章页面
@blueprint_pages.route('/pages', methods=['GET'])
def pages():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = '''select * from artical'''
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()


    # todo：需要做跳转到个人中心的功能
    # todo：需要通过cookie获取用户id和其他东西 会话相关
    user={"userCenterPage":"1","username":"cookie"}

    # todo：增加跳转到单页的特性
    #res是整页全部文章的数据
    res=render_template("/pages_title.html",user=user)
    for row in rows:
        res=res+render_template("/pages.html",artical=row)
    return res
#写文章页面
@blueprint_pages.route('/write', methods=['get'])
def writeHtml():
    return render_template("/post_artical.html")


#写文章方法没有页面 在/write页面调用
@blueprint_pages.route('/write', methods=['post'])
def write():
    title = request.form.get('title')
    content = request.form.get('content')
    cursor = conn.cursor()
    sql = '''insert into artical (title, content,readCount,likeCount,createDate) values (%s,%s,%s,%s,%s)'''
    cursor.execute(sql, (title, content,0,0,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    conn.commit()
    cursor.close()
    # 跳转到pages页面
    return redirect(url_for('pages_blueprint.pages'))

#写评论的方法 无页面 在page/index里被调用
@blueprint_pages.route('/writeComment/<index>', methods=['post'])
def writeComment(index):
    userName = request.form.get('userName')
    commentContent = request.form.get('commentContent')
    cursor = conn.cursor()
    sql = '''insert into comment (articalId, userName,commentContent) values (%s,%s,%s)'''
    cursor.execute(sql, (int(index),userName,commentContent))
    conn.commit()
    cursor.close()
    return redirect("/page/" + str(index))