from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from flask import redirect, url_for, request
from .. import db
from ..models import Event
from datetime import datetime, date, time
import os
from werkzeug.utils import secure_filename

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/create_event', methods=['POST', 'GET'])
@login_required
def create_event():
    if current_user.role != 'administrator':
        return redirect(url_for('main.content.list_items'))
    if request.method == 'POST':
        if(request.form['status'] == "Status"):
          flash('You need to provide a status!')
          return render_template('admin/event_editor.html', url=url_for('main.admin.create_event'), date="", time="", e={}, title="Create new event")
        new_event = Event(
            name=request.form['name'],
            type=request.form['type'],
            venue=request.form['venue'],
            datetime=datetime.combine(
                datetime.strptime(request.form['date'], "%Y-%m-%d").date(),
                datetime.strptime(request.form['time'], "%H:%M").time(),
            ),
            price=request.form['price'],
            artist=request.form['artist'],
            description=request.form['description'],
            ticketcount=request.form['ticketcount'],
            status=request.form['status'],
            creator_id=current_user.id,
        )
        db.session.add(new_event)
        db.session.commit()
        event_id = new_event.id
        img_file = request.files['file']
        filename = event_id
        BASE_PATH = os.path.dirname(__file__)
        upload_path = os.path.join(
            BASE_PATH, '../static', secure_filename(filename))
        img_file.save(upload_path)
        flash(f'New event added successfully. id: #{new_event.id}')
        return redirect(url_for('main.content.details', event_id=event_id))
    return render_template('admin/event_editor.html', url=url_for('main.admin.create_event'), date="", time="", e={}, title="Create new event")


@bp.route('/update_event', methods=['POST', 'GET'])
@login_required
def update_event():
    if current_user.role != 'administrator':
        return redirect(url_for('main.content.list_items'))
    event_id = request.args.get('event_id')
    e1 = Event.query.filter_by(id=event_id).first()
    if request.method == 'POST':
        if(request.form['status'] == "Status"):
          flash('You need to provide a status!')
          return render_template('admin/event_editor.html',
                                 url=url_for('main.admin.update_event',
                                             event_id=event_id),
                                 date=e1.datetime.date().strftime("%Y-%m-%d"),
                                 time=e1.datetime.time().strftime("%H:%M"), e=e1,
                                 title="Update the event")
        e1.name = request.form['name']
        e1.type = request.form['type']
        e1.venue = request.form['venue']
        e1.datetime = datetime.combine(
            datetime.strptime(request.form['date'], "%Y-%m-%d").date(),
            datetime.strptime(request.form['time'], "%H:%M").time(),
        )
        e1.price = request.form['price']
        e1.artist = request.form['artist']
        e1.description = request.form['description']
        e1.ticketcount = request.form['ticketcount']
        e1.status = request.form['status']
        e1.creator_id = current_user.id
        db.session.commit()
        img_file = request.files['file']
        filename = event_id
        BASE_PATH = os.path.dirname(__file__)
        upload_path = os.path.join(
            BASE_PATH, '../static', secure_filename(filename))
        img_file.save(upload_path)
        flash(f'#{event_id} updated successfully.')
        return redirect(url_for('main.admin.update_event', event_id=event_id))
    return render_template('admin/event_editor.html',
                           url=url_for('main.admin.update_event',
                                       event_id=event_id),
                           date=e1.datetime.date().strftime("%Y-%m-%d"),
                           time=e1.datetime.time().strftime("%H:%M"), e=e1,
                           title="Update the event")


@bp.route('/delete_event')
@login_required
def delete_event():
    if current_user.role != 'administrator':
        return redirect(url_for('main.content.list_items'))
    event_id = request.args.get('event_id')
    e1 = Event.query.filter_by(id=event_id).first()
    db.session.delete(e1)
    db.session.commit()
    flash(f'{event_id}# event deleted successfully.')
    return redirect(url_for('main.content.list_items'))
