#query all users in the DB
User.query.all

#delete event
delete from app.models import Booking, Event
from flask.helpers import url_for
from Event where 'id'='1'

#list_items by type
Event.query.filter_by(type='active').all
Event.query.filter_by(type='inactive').all
Event.query.filter_by(type='upcoming').all

# Order by a field
Event.query.order_by(Event.creator_id).all()

#Update  comment
@bp.roure('/<id>/comment',methods = ['GET','POST'])
def comment(id):
    form = CommentForm()
    #get the event object associated to the page and the commet
    event_ojt = Event.query.filter_by(id=id).first
    if form.validate_on-submit():
        #read the commment from the form
        comment = Comment(text.form.text.datatime,event=event_obj)
        db.session.add(comment)
        db.session.commit()
        print('Your comment has been added','success')
    return redirect(url_for('event',id=id))

#get comment by event_id
Event.query.filter_by(event.id).all

#remain tickets
ticket_count = Event.query(ticketcount).filter_by(id=1)
select sum(quantity) as sumvalue from Booking where 'event_id'='1'


#booking_history by user_id
Booking.query.filter_by(user_id='1').all

#booking_history by event_id
Booking.query.filter_by(event_id='1').all

