from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(32), index=False, nullable=False)
    username = db.Column(db.String(128), index=True,
                         unique=True, nullable=False)
    emailid = db.Column(db.String(128), index=False, nullable=False)
    phonenumber = db.Column(db.String(128), index=False, nullable=False)
    address = db.Column(db.String(128), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    # relation to call user.comments and comment.user
    comments = db.relationship('Comment', backref='user')
    # relation to call user.bookings and booking.user
    bookings = db.relationship('Booking', backref='user')

    def __repr__(self):  # string print method
        return "<id: {}, name: {}>".format(self.id, self.name)


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, nullable=False)
    type = db.Column(db.String(64), nullable=False)
    venue = db.Column(db.String(128), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Integer)
    artist = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(384), nullable=False)
    ticketcount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(64), nullable=False)
    creator_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    # relation to call event.comments and comment.event
    comments = db.relationship('Comment', backref='events')

    def __repr__(self):  # string print method
        return "<id: {}, name: {}>".format(self.id, self.name)


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    payment = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __repr__(self):  # string print method
        return "<id: {}, user: {}, event: {}>".format(self.id, self.user_id, self.event_id)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(512))
    created_at = db.Column(db.DateTime)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __repr__(self):
        return "<id: {}, Comment: {}, Creator: {}>".format(self.id, self.text, self.creator_id)
