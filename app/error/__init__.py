from flask import Blueprint, render_template

bp = Blueprint('error', __name__)

#   allows users to navigate back to the landing/home page
# /error - internal server errors


@bp.errorhandler(Exception)
def error():
    return render_template('error/error.html')


# /error/404 - page not found
@bp.errorhandler(404)
def error_404(e):  # error view function
    return render_template('error/404.html'), 404
