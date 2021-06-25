from typing import Text
from app.models import Booking, Comment, Event, User
from app import db
from app import create_app

app = create_app()

ctx = app.app_context()
ctx.push()

db.create_all()

# password123
default_password = 'pbkdf2:sha256:150000$G5ava6EK$581216dac4b0a3ab261a6b828dffd575ff073a58949a9a95f5d682d2df35c0fa'

# creat user objects
user1 = User(role='administrator', username='admin1', emailid='admin1@ta.com',
             phonenumber='4783573230', password_hash=default_password, address='1165 Yorba Manor')
db.session.add(user1)

user2 = User(role='administrator', username='admin2', emailid='admin2@ta.com',
             phonenumber='5780817439', password_hash=default_password, address='818 Crestmont Turnpike')
db.session.add(user2)

user3 = User(role='customer', username='customer1', emailid='customer1@ta.com',
             phonenumber='9904535198', password_hash=default_password, address='1116 Pennsylvania Stravenue')
db.session.add(user3)

user4 = User(role='customer', username='customer2', emailid='customer2@ta.com',
             phonenumber='5005692608', password_hash=default_password, address='1165 Yorba Manor')
db.session.add(user4)

user5 = User(role='customer', username='customer3', emailid='customer3@ta.com',
             phonenumber='5005692699', password_hash=default_password, address='1168 Yorba Manor')
db.session.add(user5)

db.session.commit()
db.session.close()

# create events  may have some mistakes
event1 = Event(id='1',name='event1',type='type1',venue='square1',datetime='',price='500',artist='artist1',
description='An interesting concert',ticketcount='7000',status='active',creador_id= user1.id)
db.session.add(event1)

event2 = Event(id='2',name='event2',type='type2',venue='square2',datetime='',price='400',artist='artist2',
description='Forest Concert',ticketcount='8000',status='inactive',creador_id= user2.id)
db.session.add(event2)

event3 = Event(id='3',name='event3',type='type3',venue='square3',datetime='',price='300',artist='artist3',
description='Strawberry Music Festival',ticketcount='10000',status='upcoming',creador_id= user1.id)
db.session.add(event3)

event4 = Event(id='4',name='event4',type='type2',venue='square4',datetime='',price='700',artist='artist4',
description='Classical comcert',ticketcount='5000',status='active',creador_id= user2.id)
db.session.add(event4)

event5 = Event(id='5',name='event5',type='type1',venue='square2',datetime='',price='900',artist='artist5',
description='Special comcert',ticketcount='5000',status='active',creador_id= user2.id)
db.session.add(event5)

#create booking
booking1 = Booking(datetime='',quantity='9',price='700',payment='6300',user_id=user3.id,event_id=event4.id)
db.session.add(booking1)

booking2 = Booking(datetime='',quantity='3',price='300',payment='900',user_id=user4.id,event_id=event3.id)
db.session.add(booking2)

booking3 = Booking(datetime='',quantity='5',price='400',payment='2000',user_id=user5.id,event_id=event2.id)
db.session.add(booking2)

#create comment
comment1=Comment(text='Good',creator_id=user3.id)
db.session.add(comment1)

comment2=Comment(text='Perfect!',creator_id=user4.id)
db.session.add(comment2)

comment3=Comment(text='Excellent!',creator_id=user5.id)
db.session.add(comment3)