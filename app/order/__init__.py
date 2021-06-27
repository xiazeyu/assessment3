from flask import Blueprint,render_template, flash, redirect, url_for
from flask_login import login_required

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/book')
@login_required
#   provide quantity
#   Booked out cannot be placed if exceeds the tickets available
def book():

    flash('booking successfuly.')
    return redirect(url_for('main.content.list_items'))


@bp.route('/booking_history')
@login_required
def booking_history():
    return render_template('order/booking_history.html')
