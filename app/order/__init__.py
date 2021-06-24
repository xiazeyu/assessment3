from flask import Blueprint,render_template

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/book')
#   provide quantity
#   Booked out cannot be placed if exceeds the tickets available
def book():
    return render_template('order/book_result.html')


@bp.route('/booking_history')
def booking_history():
    return render_template('order/booking_history.html')
