from flask import Blueprint,render_template

bp = Blueprint('content', __name__)


@bp.route('/', methods=['GET', 'POST'])
# / - landing page
#   clearly conveys what kind of events the website promotes
#   some upcoming events
#   browse the events by category
#   useful overview of the events
#   information including event status
# /?category=<str> - landing page with specific category
def list_items():
     return render_template ('content/list_items.html')


@bp.route('/details', methods=['GET', 'POST')
# /details?event_id=<int> - detail page of the event
#   image description date other
def details():
     return render_template ('content/detials.html')


@bp.route('/new_comment', methods=['GET', 'POST')
# /new_comment?event_id=<int> - new comment event handler
#   author review date
def new_comment():
     return render_template ('content/detials.html')
