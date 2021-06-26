from typing import Text
from app.models import Booking, Comment, Event, User
from app import db
from app import create_app
from datetime import datetime

app = create_app()

ctx = app.app_context()
ctx.push()

db.create_all()

# password123
default_password = 'pbkdf2:sha256:150000$G5ava6EK$581216dac4b0a3ab261a6b828dffd575ff073a58949a9a95f5d682d2df35c0fa'


def pt(s):
    return datetime.strptime(s, "%Y-%m-%d %H:%M")


# creat user objects
user1 = User(id='1', role='administrator', username='admin1', emailid='admin1@ta.com',
             phonenumber='4783573230', password_hash=default_password, address='1165 Yorba Manor')
db.session.add(user1)

user2 = User(id='2', role='administrator', username='admin2', emailid='admin2@ta.com',
             phonenumber='5780817439', password_hash=default_password, address='818 Crestmont Turnpike')
db.session.add(user2)

user3 = User(id='3', role='customer', username='customer1', emailid='customer1@ta.com',
             phonenumber='9904535198', password_hash=default_password, address='1116 Pennsylvania Stravenue')
db.session.add(user3)

user4 = User(id='4', role='customer', username='customer2', emailid='customer2@ta.com',
             phonenumber='5005692608', password_hash=default_password, address='1165 Yorba Manor')
db.session.add(user4)

user5 = User(id='5', role='customer', username='customer3', emailid='customer3@ta.com',
             phonenumber='5005692699', password_hash=default_password, address='1168 Yorba Manor')
db.session.add(user5)

a = User(id='233', role='administrator', username='a', emailid='a@ta.com',
         phonenumber='1', password_hash='pbkdf2:sha256:260000$wg9qSdzPVpxIof7O$fe16f29e1eb826ca7f4a00974551268f896e8ff36e8250ec03e4337479ae59df', address='1168 Yorba Manor')
db.session.add(a)

# create events  may have some mistakes
event1 = Event(id='1', name='event1', type='classical', venue='square1', datetime=pt('2021-07-04 13:32'), price='500', artist='artist1',
               description='An interesting concert', ticketcount='7000', status='active', creator_id=a.id)
db.session.add(event1)

event2 = Event(id='2', name='event2', type='pop', venue='square2', datetime=pt('2021-04-01 15:32'), price='400', artist='artist2',
               description='Forest Concert', ticketcount='8000', status='inactive', creator_id=user2.id)
db.session.add(event2)

event3 = Event(id='3', name='event3', type='classical', venue='square3', datetime=pt('2021-12-05 08:32'), price='300', artist='artist3',
               description='Strawberry Music Festival', ticketcount='10000', status='upcoming', creator_id=user1.id)
db.session.add(event3)

event4 = Event(id='4', name='event4', type='pop', venue='square4', datetime=pt('2021-01-11 11:32'), price='700', artist='artist4',
               description='Classical comcert', ticketcount='5000', status='active', creator_id=user2.id)
db.session.add(event4)

event5 = Event(id='5', name='event5', type='vocal', venue='square2', datetime=pt('1990-12-21 02:32'), price='900', artist='artist5',
               description='Special comcert', ticketcount='5000', status='active', creator_id=user2.id)
db.session.add(event5)

# create booking
booking1 = Booking(datetime=pt('1990-12-21 02:32'), quantity='9', price='700',
                   payment='6300', user_id=a.id, event_id=event4.id)
db.session.add(booking1)

booking2 = Booking(datetime=pt('2021-12-05 08:32'), quantity='3', price='300',
                   payment='900', user_id=a.id, event_id=event3.id)
db.session.add(booking2)

booking3 = Booking(datetime=pt('2021-07-04 13:32'), quantity='5', price='400',
                   payment='2000', user_id=user5.id, event_id=event2.id)
db.session.add(booking2)

# create comment
comment1 = Comment(text='Good', creator_id=a.id,
                   created_at=pt('1990-12-21 02:32'), event_id=event1.id)
db.session.add(comment1)

comment2 = Comment(text='Perfect!', creator_id=user4.id,
                   created_at=pt('1990-12-21 02:32'), event_id=event1.id)
db.session.add(comment2)

comment3 = Comment(text='Excellent!', creator_id=user5.id,
                   created_at=pt('1990-12-21 02:32'),
                   event_id=event2.id)
db.session.add(comment3)

db.session.commit()
db.session.close()
