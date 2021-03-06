#coding:utf-8
from flask import Flask, url_for,render_template

app = Flask(__name__)

name = 'Zac Zhang'
movies = [
    {'title':'My Neighbor Toronto', 'year':'1998'},
    {'title':	'Dead	Poets	Society',	'year':	'1989'},
    {'title':	'A	Perfect	World',	'year':	'1993'},
    {'title':	'Leon',	'year':	'1994'},
    {'title':	'Mahjong',	'year':	'1996'},
    {'title':	'Swallowtail	Butterfly',	'year':	'1996'},
    {'title':	'King	of	Comedy',	'year':	'1999'},
    {'title':	'Devils	on	the	Doorstep',	'year':	'1999'},
    {'title':	'WALL-E',	'year':	'2008'},
    {'title':	'The	Pork	of	Music',	'year':	'2012'},
]

#render_template用作模板渲染函数，第一个参数是模板，所在根目录为templates文件夹，后面的参数为模板中的变量
@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return "User:%s"%name

#url_for函数：用来生成url，第一个参数是路由端点值，默认为视图函数的名称（装饰器内的url部分）
@app.route('/test')
def test_url_for():
    print(url_for('user_page',name='zac'))
    print(url_for('test_url_for',num='2'))
    return 'Test_page'

