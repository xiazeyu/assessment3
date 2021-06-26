from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from flask import redirect, url_for, request
from .. import db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/create_event')
@login_required
#   Upcoming, Inactive, Booked, or Cancelled
def create_event():
    if current_user.role != 'administrator':
      return redirect(url_for('main.content.list_items'))
    return render_template ('admin/event_editor.html')


@bp.route('/update_event')
@login_required
# /admin/update_event?event_id=<int> - update event
def update_event():
    if current_user.role != 'administrator':
      return redirect(url_for('main.content.list_items'))
    return render_template ('admin/event_editor.html')


@bp.route('/delete_event')
@login_required
# /admin/delete_event?event_id=<int> - delete event
def delete_event():
    if current_user.role != 'administrator':
      return redirect(url_for('main.content.list_items'))
    event_id = request.args.get('event_id')
    flash()
    return render_template ('content/list_items.html')
