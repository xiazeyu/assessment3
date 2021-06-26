from flask import (
    Blueprint, flash, render_template, request, url_for, redirect
)
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import LoginForm, RegisterForm
from ..models import User
from flask_login import login_user, login_required, logout_user
from .. import db
bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None
    if login_form.validate_on_submit():
        user_name = login_form.user_name.data
        password = login_form.password.data
        u1 = User.query.filter_by(username=user_name).first()
        if u1 is None:
            error = 'Incorrect user name'
        elif not check_password_hash(u1.password_hash, password):
            error = 'Incorrect password'
        if error is None:
            login_user(u1)
            next = request.args.get('next')
            return redirect(next or url_for('main.content.list_items'))
        else:
            flash(error)
    return render_template('user/login.html', form=login_form, heading="Login")


@bp.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    error = None
    if register_form.validate_on_submit():
        role = register_form.role.data
        user_name = register_form.user_name.data
        email_id = register_form.email_id.data
        password = register_form.password.data
        phonenumber = register_form.phonenumber.data
        address = register_form.address.data
        u1 = User.query.filter_by(username=user_name).first()
        if u1 is not None:
            error = 'user name alreday registered'
        if error is None:
            pwd_hash = generate_password_hash(password)
            new_user = User(username=user_name,
                            password_hash=pwd_hash,
                            emailid=email_id,
                            phonenumber=phonenumber,
                            role=role,
                            address=address,
                            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.user.login'))
        else:
            flash(error)

    return render_template('user/register.html', form=register_form, heading="Register")


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.content.list_items'))
