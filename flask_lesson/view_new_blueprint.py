from flask import Blueprint

#todo:通过使用blueprint 解决循环依赖的问题
#todo：view 依赖blueprint model依赖view 并在model中注册blueprint
index_blueprint=Blueprint("my_test_blueprint",__name__)
@index_blueprint.route('/')
def hello_world():
    return 'hello_world'