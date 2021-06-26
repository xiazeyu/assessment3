from typing import Text
from app.models import Booking, Comment, Event, User
from app import db
from app import create_app

app = create_app()

ctx = app.app_context()
ctx.push()

db.create_all()

# create events  （may have some mistakes）
event1 = Event(id='1',name='event1',type='type1',venue='square1',datetime='2021-7-1',price='500',artist='artist1',
description='An interesting concert',ticketcount='7000',status='active')
db.session.add(event1)

event2 = Event(id='2',name='event2',type='type2',venue='square2',datetime='2021-7-7',price='400',artist='artist2',
description='Forest Concert',ticketcount='8000',status='inactive')
db.session.add(event2)

event3 = Event(id='3',name='event3',type='type3',venue='square3',datetime='2021-6-30',price='300',artist='artist3',
description='Strawberry Music Festival',ticketcount='10000',status='upcoming')
db.session.add(event3)

event4 = Event(id='4',name='event4',type='type2',venue='square4',datetime='2021-7-5',price='700',artist='artist4',
description='Classical comcert',ticketcount='5000',status='active')
db.session.add(event4)

event5 = Event(id='5',name='event5',type='type1',venue='square2',datetime='2021-7-4',price='900',artist='artist5',
description='Special comcert',ticketcount='5000',status='active')
db.session.add(event5)

db.session.commit()
db.session.close()

#create booking
booking1 = Booking(datetime='',quantity='9',price='700',payment='6300',user_id=user3.id,event_id=event4.id)
db.session.add(booking1)

booking2 = Booking(datetime='',quantity='3',price='300',payment='900',user_id=user4.id,event_id=event3.id)
db.session.add(booking2)

booking3 = Booking(datetime='',quantity='5',price='400',payment='2000',user_id=user5.id,event_id=event2.id)
db.session.add(booking2)


db.session.commit()
db.session.close()

#create comment
comment1=Comment(text='Good',creator_id=user3.id,event_id=event1.id)
db.session.add(comment1)

comment2=Comment(text='Perfect!',creator_id=user4.id,event_id=event1.id)
db.session.add(comment2)

comment3=Comment(text='Excellent!',creator_id=user5.id,event_id=event2.id)
db.session.add(comment3)

db.session.commit()
db.session.close()


# delete event
delete from app.models import Booking, Event

# list_items by type
Event.query.filter_by(type='active').all
Event.query.filter_by(type='inactive').all
Event.query.filter_by(type='upcoming').all

# Order by a field
Event.query.order_by(Event.creator_id).all()

# Update  comment


@bp.roure('/<id>/comment', methods=['GET', 'POST'])
def comment(id):
    form = CommentForm()
    # get the event object associated to the page and the commet
    event_ojt = Event.query.filter_by(id=id).first
    if form.validate_on-submit():
        # read the commment from the form
        comment = Comment(text.form.text.datatime, event=event_obj)
        db.session.add(comment)
        db.session.commit()
        print('Your comment has been added', 'success')
    return redirect(url_for('event', id=id))


# get comment by event_id
Event.query.filter_by(event.id).all

# remain tickets (unfinished)
ticket_count = Event.query(ticketcount).filter_by(id=1)
select sum(quantity) as sumvalue from Booking where 'event_id' = '1'


# booking_history by user_id
Booking.query.filter_by(user_id='1').all

# booking_history by event_id
Booking.query.filter_by(event_id='1').all
