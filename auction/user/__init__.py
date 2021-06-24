from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/login')
# as customer or as admin
def login():
    pass


@bp.route('/register')
# name, email-id, password, contact number, and address
#   as customer or as admin
def register():
    pass


@bp.route('/logout')
def logout():
    pass
