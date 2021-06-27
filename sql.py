
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
