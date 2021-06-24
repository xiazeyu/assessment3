from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login')
# as customer or as admin
def login():
    return 'login'


@bp.route('/register')
# name, email-id, password, contact number, and address
#   as customer or as admin
def register():
    return 'register'


@bp.route('/logout')
def logout():
    return 'logout'
