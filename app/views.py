from werkzeug.exceptions import HTTPException
from . import admin, content, order, user
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


bp.register_blueprint(admin.bp)
bp.register_blueprint(content.bp)
bp.register_blueprint(order.bp)
bp.register_blueprint(user.bp)


@bp.app_errorhandler(Exception)
def error(e):
    response = e.get_response()
    return render_template('error/error.html', code=e.code, name=e.name, description=e.description)
