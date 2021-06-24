from flask import Blueprint

bp = Blueprint('content', __name__)


@bp.route('/')
# / - landing page
#   clearly conveys what kind of events the website promotes
#   some upcoming events
#   browse the events by category
#   useful overview of the events
#   information including event status
# /?category=<str> - landing page with specific category
def list_items():
    return 'list_items'


@bp.route('/details')
# /details?event_id=<int> - detail page of the event
#   image description date other
def details():
    return 'details'


@bp.route('/new_comment')
# /new_comment?event_id=<int> - new comment event handler
#   author review date
def new_comment():
    return 'new_comment'
