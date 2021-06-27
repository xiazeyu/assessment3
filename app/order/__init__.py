from flask import Blueprint, render_template, flash, redirect, url_for, request
from ..models import Booking, Comment, Event, User
from flask_login import login_required, current_user
from datetime import datetime
from sqlalchemy import func
from .. import db

bp = Blueprint('order', __name__, url_prefix='/order')


@bp.route('/book', methods=['POST', 'GET'])
@login_required
def book():
    event_id = request.args.get('event_id')
    event = Event.query.filter_by(id=event_id).first()
    quantity = int(request.form['quantity'])
    booked_tickets = db.session.query(
        func.sum(Booking.quantity)).filter(event_id == event_id).scalar()
    remain_tickets = event.ticketcount - booked_tickets
    if quantity <= 0:
      flash('Quantity must be positive.')
      return redirect(url_for('main.content.details', event_id=event_id))
    if remain_tickets < quantity:
      flash('You are ordering more than remaining tickets, so order cannot be processed.')
      return redirect(url_for('main.content.details', event_id=event_id))
    new_booking = Booking(
        datetime=datetime.now(),
        quantity=request.form['quantity'],
        price=Event.query.filter_by(
            id=event_id).first().price * quantity,
        payment=request.form['payment'],
        user_id=current_user.id,
        event_id=event_id,
    )
    if remain_tickets == quantity:
      event.status = 'booked'
    db.session.add(new_booking)
    db.session.commit()
    flash(f'booking successfuly, your order id is #{new_booking.id}')
    return redirect(url_for('main.order.booking_history'))


@bp.route('/booking_history', methods=['POST', 'GET'])
@login_required
def booking_history():
    orders = Booking.query.filter_by(
        user_id=current_user.id).all()
    if current_user.role == 'administrator':
        flash('Administrator sees all events.')
        orders = Booking.query.all()
    for item in orders:
        item.event_name = Event.query.filter_by(
            id=item.event_id).first().name
        item.dt = item.datetime.strftime("%Y-%m-%d %H:%M")
    return render_template('order/booking_history.html', orders=orders)
