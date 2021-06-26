from flask import Blueprint,render_template, flash, redirect, url_for

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/book')
#   provide quantity
#   Booked out cannot be placed if exceeds the tickets available
def book():
    
    flash('booking successfuly.')
    return redirect(url_for('main.content.list_items'))


@bp.route('/booking_history')
def booking_history():
    return render_template('order/booking_history.html')
