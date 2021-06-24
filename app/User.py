from app import db
from app.models import User
from app import create_app

app = create_app()

ctx = app.app_context()
ctx.push()

db.create_all()

#creat first user object
user1 = User(id='1',name='Tina',emailid='2544505726@qq.com',phonenumber='18021870939',password_hash='test')
db.session.add(user1)

user2 = User(id='2',name='Peter',emailid='123456789@qq.com',phonenumber='18021899999',password_hash='test')
db.session.add(user2)

user3 = User(id='3',name='Andy',emailid='123456799@qq.com',phonenumber='180219998999',password_hash='test')
db.session.add(user3)

user4 = User(id='4',name='Alex',emailid='123456779@qq.com',phonenumber='180219668999',password_hash='test')
db.session.add(user4)
