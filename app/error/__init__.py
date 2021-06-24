from flask import Blueprint,render_template

bp = Blueprint('error', __name__, url_prefix='/error')

#   allows users to navigate back to the landing/home page
# /error - internal server errors
@bp.route('/')
def error():
  return render_template('error/error.html')
  


# /error/404 - page not found
@bp.route(404)
def error_404(e): #error view function
  return render_template('error/404.html'),404