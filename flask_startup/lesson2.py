# 在命令行执行python3 lesson2.py
# curl http://localhost:8080/hi
import requests
from flask import Flask
from requests import Session

app = Flask(__name__)

# 指定仅监听GET方法
@app.route('/hi', methods=['GET'])
def hi():
    return 'hi'
    
# debug模式开启后,改动代码会自动重启服务器,这样改完代码不用再手动重启服务器了
app.run(debug=True, port=8080)