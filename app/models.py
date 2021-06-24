class User(db.Model):
    __table.name__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    phonenumber = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    # relation to call user.comments and comment.user
    comments = db.relationship('Comment', backref='user')
def __repr__(self): #string print method
    return "<Name: {}, ID: {}>".format(self.name, self.id)  

class Destination(db.Model):
    __table.name__= 'destinations' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),index=True,nullable=False)
    type = db.Column(db.String(100))
    venue = db.Column(db.String(100))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    artist = db.Column(db.String(100))
    description = db.Column(db.String(300))
    ticketcount = db.Column(db.Integer)
    # relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='destination')
def __repr__(self): #string print method
    return "<Name: {}>".format(self.name)

class Booking(db.Model):
    __table.name__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    qunantity = db.Column(db.Integer)
    payment = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer,db.ForeignKey('destinations.id'))
    

class Comment(db.Model):
    __table.name__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
def __repr__(self):
    return "<Comment: {}>".format(self.text)

