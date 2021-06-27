from flask import Blueprint, render_template, request
from flask_login import login_required
from .. import db

bp = Blueprint('content', __name__, url_prefix='/content')


@bp.route('/list_items')
# / - landing page
#   some upcoming events
#   browse the events by category
#   useful overview of the events
#   information including event status
# /?category=<str> - landing page with specific category
def list_items():
    type = request.args.get('type') or 'vocal'
    return render_template('content/list_items.html', type=type)


@bp.route('/details')
@login_required
# /details?event_id=<int> - detail page of the event
#   image description date other
def details():
    return render_template('content/details.html')


@bp.route('/new_comment')
@login_required
# /new_comment?event_id=<int> - new comment event handler
#   author review date
def new_comment():
    return render_template('content/details.html')
