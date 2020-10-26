#coding:utf-8
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/user/<name>')
def user_page(name):
    return "User:%s"%name

#url_for函数：用来生成url，第一个参数是路由端点值，默认为视图函数的名称（装饰器内的url部分）
@app.route('/test')
def test_url_for():
    print(url_for('user_page',name='zac'))
    print(url_for('test_url_for',num='2'))
    return 'Test_page'
