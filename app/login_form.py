from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
 
 
class LoginForm(Form):
    accountNumber = StringField('accountNumber', validators=[DataRequired('accountNumber is null')])
    password = PasswordField('password', validators=[DataRequired('password is null')])

from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')
def index():
    return  "<h1>主页</h1>"

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/login2/')
def login2():
    # 获取用户输入的用户名
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    # 逻辑处理， 用来判断用户和密码是否正确;
    if username == 'root' and password == 'redhat':
        # 重定向到指定路由；
        return  redirect('/')
        # return "登录成功"
    else:
        return  "登录失败"

if __name__ == '__main__':
    app.run()
