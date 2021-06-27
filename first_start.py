print('NORMALLY YOU SHOULD NOT USE THIS SCRIPT AGAIN')
print('IF YOU KNOW WHAT YOU ARE DOING, REMOVE THE FOLLOWING LINE.')
exit()

# Remember to remove database.db manually

from typing import Text
from app.models import Booking, Comment, Event, User
from app import db
from app import create_app
from datetime import datetime

app = create_app()

ctx = app.app_context()
ctx.push()

db.create_all()

db.session.commit()
db.session.close()
