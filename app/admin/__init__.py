from flask import Blueprint,render_template
from flask_login import login_required, current_user
from .. import db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/create_event')
@login_required
#   Upcoming, Inactive, Booked, or Cancelled
def create_event():
    if current_user.role != 'administrator':
      return 0
    return render_template ('admin/event_editor.html')


@bp.route('/update_event')
@login_required
# /admin/update_event?event_id=<int> - update event
def update_event():
    return render_template ('admin/event_editor.html')


@bp.route('/delete_event')
@login_required
# /admin/delete_event?event_id=<int> - delete event
def delete_event():
    return render_template ('content/list_items.html')
