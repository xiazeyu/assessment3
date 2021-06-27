from typing import Text
from app.models import Booking, Comment, Event, User
from app import db
from app import create_app

app = create_app()

ctx = app.app_context()
ctx.push()

db.create_all()

# create events  （may have some mistakes）
event1 = Event(id='1',name='event1',type='classical',venue='square1',datetime='2021-07-04 13:32:00.000000',price='500',artist='artist1',
description='a',ticketcount='7000',status='active',creator_id='233')
db.session.add(event1)

event2 = Event(id='2',name='event2',type='pop',venue='square2',datetime='2021-04-01 15:32:00.000000',price='400',artist='artist2',
description='Forest Concert',ticketcount='8000',status='inactive',creator_id='2')
db.session.add(event2)

event3 = Event(id='3',name='event3',type='classical',venue='square3',datetime='2021-04-01 15:32:00.000000',price='300',artist='artist3',
description='Strawberry Music Festival',ticketcount='10000',status='upcoming',creator_id='1')
db.session.add(event3)

event4 = Event(id='4',name='event4',type='pop',venue='square4',datetime='2021-01-11 11:32:00.000000',price='700',artist='artist4',
description='Classical comcert',ticketcount='5000',status='active',creator_id='2')
db.session.add(event4)
s
event5 = Event(id='5',name='event5',type='vocal',venue='square2',datetime='2020-12-21 02:32:00.000000',price='900',artist='artist5',
description='Special comcert',ticketcount='5000',status='active',creator_id='2')
db.session.add(event5)

db.session.commit()
db.session.close()

#create booking
booking1 = Booking(datetime='2020-6-25 02:32:00.000000',quantity='9',price='700',payment='6300',user_id='3',event_id='4')
db.session.add(booking1)

booking2 = Booking(datetime='2021-06-05 08:32:00.000000',quantity='3',price='300',payment='900',user_id='4',event_id='3')
db.session.add(booking2)






db.session.commit()
db.session.close()

#create comment
comment1=Commdaent(text='Good',creat_at='2021-7-20 02:32:00.000000',creator_id='3',event_id='1')
db.session.add(comment1)

comment2=Comment(text='Perfect!',creat_at='2021-7-1 02:32:00.000000',creator_id='4',event_id='1')
db.session.add(comment2)

comment3=Comment(text='Excellent!',creat_at='2020-12-21 02:32:00.000000',creator_id='5',event_id='2')
db.session.add(comment3)

db.session.commit()
db.session.close()


# delete event
#delete uses id from 1-3
 users = self.db.query(User).filter(User.id.in_(1,2,3)).all()
        [self.db.delete(u) for u in users]
        self.db.commit()

#delete the first Event
 event = session.query(Event).first()
    session.delete(event)
    session.db.commit()

# list_items event by type
Event.query.filter_by(type='classical').all
Event.query.filter_by(type='pop').all
Event.query.filter_by(type='vocal').all

# Order by a field
Event.query.order_by(Event.creator_id).all()

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
person = session.query(event).get(comment)

#update the price of event 1
event = session.query(Event).first()
person.price = '600'
session.db.commit()

# remain tickets 
    #add the number of booked tickets of event4
booked_tickets = db.session.query(func.sum(quanity)).filter(event.id==4).scalar()
ticket_count = Event.query.filter_by(event.id=='4')
remain_tickets= list(set(ticket_count) - set(booked_tickets)) 

# booking_history by user_id
Booking.query.filter_by(user_id='1').all

# booking_history by event_id
Booking.query.filter_by(event_id='1').all
