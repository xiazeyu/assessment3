from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, RegisterForm
from ..models import User
from flask_login import login_user, login_required, logout_user

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login', methods=['GET', 'POST'])
def login():  # view function
    print('In Login View function')
    login_form = LoginForm()
    error = None
    if(login_form.validate_on_submit() == True):
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(username=user_name).first()
        if u1 is None:
            error = 'Incorrect user name'
        # takes the hash and password
        elif not check_password_hash(u1.password_hash, password):
            error = 'Incorrect password'
        if error is None:
            login_user(u1)
            # this gives the url from where the login page was accessed
            nextp = request.args.get('next')
            print(nextp)
            #if next is None or not nextp.startswith('/'):
            return redirect(url_for('main.content.list_items'))
            #return redirect(nextp)
        else:
            flash(error)
    return render_template('user/login.html', form=login_form)


@bp.route('/register')
# name, email-id, password, contact number, and address
#   as customer or as admin
def register():
    return render_template('user/register.html')


@bp.route('/logout')
def logout():
    return render_template('user/login.html')
