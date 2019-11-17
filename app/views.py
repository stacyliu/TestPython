from flask import Blueprint

#1.在路由的页面 创建蓝图 index_blueprint
#2.在当前蓝图注册路由
#3.在manage里注册这个蓝图
#相当于一些页面从属于一个蓝图 在manage里注册蓝图相当于允许manage使用这个蓝图的页面

index_blueprint=Blueprint("my_test_blueprint",__name__)
@index_blueprint.route('/')
def hello_world():
    return 'hello_world'