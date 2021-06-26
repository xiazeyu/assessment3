from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from flask import redirect, url_for, request
from .. import db
from ..models import Event

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/create_event', methods=['POST', 'GET'])
@login_required
def create_event():
    if current_user.role != 'administrator':
        return redirect(url_for('main.content.list_items'))
    if request.method == 'POST':
        new_event = Event(
            name=request.form['name'],
            type=request.form['type'],
            venue=request.form['venue'],
            datetime=request.form['datetime'],
            price=request.form['price'],
            artist=request.form['artist'],
            description=request.form['description'],
            ticketcount=request.form['ticketcount'],
            status=request.form['status'],
            creator_id=current_user.id,
        )
        db.session.add(new_event)
        db.session.commit()
        flash('New event added successfully.')
        return redirect(url_for('main.admin.create_event'))
    return render_template('admin/event_editor.html', e={}, title="Create new event")


@bp.route('/update_event', methods=['POST', 'GET'])
@login_required
def update_event():
    if current_user.role != 'administrator':
        return redirect(url_for('main.content.list_items'))
    event_id = request.args.get('event_id')
    e1 = Event.query.filter_by(id=event_id).first()
    if request.method == 'POST':
        new_event = Event(
            name=request.form['name'],
            type=request.form['type'],
            venue=request.form['venue'],
            datetime=request.form['datetime'],
            price=request.form['price'],
            artist=request.form['artist'],
            description=request.form['description'],
            ticketcount=request.form['ticketcount'],
            status=request.form['status'],
            creator_id=current_user.id,
        )
        # TODO
        flash(f'#{event_id} updated successfully.')
        return redirect(url_for('main.admin.update_event', event_id=event_id))
    render_template('admin/event_editor.html', e=e1, title="Update the event")


@bp.route('/delete_event')
@login_required
def delete_event():
    if current_user.role != 'administrator':
        return redirect(url_for('main.content.list_items'))
    event_id = request.args.get('event_id')
    # TODO
    flash(f'{event_id}# event deleted successfully.')
    return redirect(url_for('main.content.list_items'))
