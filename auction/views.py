from flask import Blueprint

bp = Blueprint('main', __name__)

# / - landing page
# /?category=<str> - landing page with specific category
# /details?event_id=<int> - detail page of the event

# /login - login page
# /register - register page
# /logout - logout

# /book?event_id=<int> - booking detailed order
# /new_comment?event_id=<int> - new comment event handler
# /booking_history - booking history

# /admin/create_event - create event
# /admin/update_event?event_id=<int> - update event
# /admin/delete_event?event_id=<int> - delete event

# /error/404 - page not found
# /error - internal server errors

@bp.route('/')
def index():
    return '<h1>Starter code for the assessment<h1>'
