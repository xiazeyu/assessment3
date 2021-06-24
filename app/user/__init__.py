from flask import Blueprint,render_template

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login')
# as customer or as admin
def login():
     return render_template('user/login.html')


@bp.route('/register')
# name, email-id, password, contact number, and address
#   as customer or as admin
def register():
   return render_template('user/register.html')


@bp.route('/logout')
def logout():
    return render_template('user/login.html')
