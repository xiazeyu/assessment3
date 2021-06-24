from auction.user.test_user import User
from auction.user.forms import LoginForm, get_user
from flask import render_template, redirect, url_for, request
from flask_login import login_user
# ...
@app.route('/login/', methods=('GET', 'POST'))  # 登录
def login():
    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_info = get_user(user_name)  # 从用户数据中查找用户记录
        if user_info is None:
            emsg = "Wrong username or password"
        else:
            user = User(user_info)  # 创建用户实体
            if user.verify_password(password):  # 校验密码
                login_user(user)  # 创建用户 Session
                return redirect(request.args.get('next') or url_for('index'))
            else:
                emsg = "Wrong username or password"
    return render_template('login.html', form=form, emsg=emsg)