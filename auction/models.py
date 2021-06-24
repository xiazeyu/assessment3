class User(db.Model):
    __table.name__= 'users'
    id = db.Column((db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    phonenumber = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class Destination(db.Mobel):
    __table.name__= 'destinations' 
    id = db.Column(db.Integer, primary_key=True)
    sportname = db.Column(db.String(100),index=True,nullable=False)
    sporttype = db.Column(db.String(100))
    sportvenue = db.Column(db.String(100))
    sportdate = db.Column(db.Date)
    sporttime = db.Column(db.String(20))
    playername = db.Column(db.String(100))
    description = db.Column(db.String(400))
    totalticket = db.Column(db.Integer)
def __repr__(self): #string print method
return "<Name: {}>".format(self.name)

class booking(db.Mobel):
    __table.name__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    numaudience = db.Column(db.Integer)
    numseat = db.Column(db.Integer)
    fare = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer,db.ForeignKey('destinations.id'))

class Comment(db.Mobel):
    __table.name__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
def __repr__(self):
return "<Comment: {}>".format(self.text)

