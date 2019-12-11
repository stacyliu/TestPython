#单个文章页面
from flask import Blueprint, session
from flask import Flask, jsonify, request, redirect, url_for, render_template
import pymysql
from requests import Session
from blog_demo_app import utils
from blog_demo_app.dbConnection import conn
from blog_demo_app.utils import Utils

blueprint_login=Blueprint("login_register_blueprint",__name__)

#todo:如果是get就是展示 如果是post就是把页面上的东西提交
@blueprint_login.route('/register', methods=['get']) #展示登陆页面
def register_page():
    text={"btnMethod":"register","btnText":"注册","gotoText":"已有账号去登陆","login_or_register_method":"login"}
    #todo: 登陆和注册页面需要相互跳转 还需要写方法处理跳转
    return render_template("/login_or_register.html",text=text)


@blueprint_login.route('/register', methods=['post'])#提交登陆页面填写的表单
def register():
    username = request.form.get('username')
    userpswd = request.form.get('userpswd')
    print(username)
    print(userpswd)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #todo：********************需要查询是不是被注册了 先用服务端校验吧 js不会********************
    isUserNameRegistedSQL='''select * from users where username=%s'''
    cursor.execute(isUserNameRegistedSQL, (username,))
    row = cursor.fetchone()
    if(row!=None):
        #如果能找到 就说明已经被注册了
        return '''<a href="/register">该账号已经被注册 点击返回换个账号试试</a>'''

    #注册
    sql = '''insert into users (username, userpswd) values (%s,%s)'''
    cursor.execute(sql, (username, userpswd))
    conn.commit()
    cursor.close()
    #TODO：需要把cookie带上
    #把username userid存在session中
    session['username'] = request.form['username']
    session['userid'] = request.form['userid']
    return redirect(url_for('pages_blueprint.pages'))


@blueprint_login.route('/login', methods=['get'])
def login_page():
    text = {"btnMethod":"login","btnText": "登陆", "gotoText": "去注册", "login_or_register_method": "register"}
    # todo: 登陆和注册页面需要相互跳转 还需要写方法处理跳转
    return render_template("/login_or_register.html", text=text)


@blueprint_login.route('/login', methods=['post'])
def login():
    username = request.form.get('username')
    userpswd = request.form.get('userpswd')
    print(username)
    print(userpswd)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # todo：********************需要查询是不是被注册了 先用服务端校验吧 js不会********************
    sql = '''select * from users where username=%s and userpswd=%s '''
    cursor.execute(sql, (username, userpswd))
    cursor.close()
    row = cursor.fetchone()
    if(row==None):#该账号没有注册或账号密码错误
        #return redirect(url_for('register'))
        return '''<a href="/login">账号或密码错误 点击返回再试试</a>'''
    else:#有注册且正确
        session['username'] = username
        session['userid'] = row.get('userid')
        print("*****"+session['username']+"*****"+(session['userid']))
        return redirect(url_for('pages_blueprint.pages'))


@blueprint_login.route('/', methods=['get'])
def index():
    if(Session!=None):
        return redirect(url_for('login_register_blueprint.login'))
    else:
        return redirect(url_for('login_register_blueprint.login'))
