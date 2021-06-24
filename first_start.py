from app.models import User
from app import db
from app import create_app

app = create_app()

ctx = app.app_context()
ctx.push()

db.create_all()

# password123
default_password = 'pbkdf2:sha256:150000$G5ava6EK$581216dac4b0a3ab261a6b828dffd575ff073a58949a9a95f5d682d2df35c0fa'

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

db.session.commit()
db.session.close()
