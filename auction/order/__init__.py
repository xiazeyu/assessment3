from flask import Blueprint

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/book')
#   provide quantity
#   Booked out cannot be placed if exceeds the tickets available
def book():
    pass


@bp.route('/booking_history')
def booking_history():
    pass
