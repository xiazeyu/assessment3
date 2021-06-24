from flask import Blueprint

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/create_event')
#   Upcoming, Inactive, Booked, or Cancelled
def create_event():
    return 'create_event'


@bp.route('/update_event')
# /admin/update_event?event_id=<int> - update event
def update_event():
    return 'update_event'


@bp.route('/delete_event')
# /admin/delete_event?event_id=<int> - delete event
def delete_event():
    return 'delete_event'
