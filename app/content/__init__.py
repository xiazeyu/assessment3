from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..models import Booking, Comment, Event, User
from flask_login import login_required, current_user
from .. import db
from sqlalchemy import func
from datetime import datetime

bp = Blueprint('content', __name__, url_prefix='/content')


@bp.route('/list_items')
def list_items():
    type = request.args.get('type') or 'vocal'
    events = Event.query.filter_by(type=type).all()
    return render_template('content/list_items.html', type=type, events=events)


@bp.route('/details')
def details():
    event_id = request.args.get('event_id')
    event = Event.query.filter_by(id=event_id).first()
    booked_tickets = db.session.query(
        func.sum(Booking.quantity).filter(Booking.event_id == event_id)).scalar() or 0
    remain_tickets = event.ticketcount - booked_tickets
    comments = Comment.query.filter_by(
        event_id=event_id).all()
    for u in comments:
        u.username = User.query.filter_by(id=u.creator_id).first().username
        u.dt = u.created_at.strftime("%Y-%m-%d %H:%M")
    step = 3
    comments_grouped = [(comments[i:i + step], i)
                        for i in range(0, len(comments), step)]
    return render_template(
        'content/details.html',
        comments=comments_grouped,
        event=event,
        event_id=event_id,
        dt=event.datetime.strftime("%Y-%m-%d %H:%M"),
        remain_tickets=remain_tickets,
        creator=User.query.filter_by(id=event.creator_id).first().username
    )


@bp.route('/new_comment', methods=['POST', 'GET'])
@login_required
def new_comment():
    event_id = request.args.get('event_id')
    comment = Comment(
        text=request.form['comment_text'],
        created_at=datetime.now(),
        creator_id=current_user.id,
        event_id=event_id,
    )
    flash('Comment added successfully.')
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('main.content.details', event_id=event_id))
