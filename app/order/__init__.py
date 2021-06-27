from flask import Blueprint, render_template, flash, redirect, url_for, request
from ..models import Booking, Comment, Event, User
from flask_login import login_required, current_user
from datetime import datetime
from .. import db

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/book', methods=['POST', 'GET'])
@login_required
#   provide quantity
#   Booked out cannot be placed if exceeds the tickets available
def book():
    event_id = request.args.get('event_id')
    new_booking = Booking(

        datetime=datetime.now(),
        quantity=request.form['quantity'],
        price=Event.query.filter_by(
            id=event_id).first().price,
        payment=request.form['payment'],
        user_id=current_user.id,
        event_id=event_id,
    )
    db.session.add(new_booking)
    db.session.commit()
    flash('booking successfuly.')
    return redirect(url_for('main.order.booking_history'))


@bp.route('/booking_history', methods=['POST', 'GET'])
@login_required
def booking_history():
    orders = Booking.query.filter_by(
        user_id=current_user.id).all()
    for item in orders:
      item.event_name = Event.query.filter_by(
          id=item.event_id).first().name
      item.dt = item.datetime.strftime("%Y-%m-%d %H:%M")
    return render_template('order/booking_history.html', orders=orders)
