from flask import Blueprint

bp = Blueprint('error', __name__, url_prefix='/error')

#   allows users to navigate back to the landing/home page
# /error - internal server errors
@bp.route('/')
def error():
  pass


# /error/404 - page not found
@bp.route('/404')
def error_404():
  pass
