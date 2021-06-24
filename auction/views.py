from flask import Blueprint

bp = Blueprint('main', __name__)

from . import admin, content,error,order,user
bp.register_blueprint(admin.bp)
bp.register_blueprint(content.bp)
bp.register_blueprint(error.bp)
bp.register_blueprint(order.bp)
bp.register_blueprint(user.bp)

