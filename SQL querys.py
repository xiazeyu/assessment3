#query all users in the DB
User.query.all

#list_items by type
Event.query.filter_by(type='active').all
Event.query.filter_by(type='inactive').all
Event.query.filter_by(type='upcoming').all

# Order by a field
Event.query.order_by(Event.creator_id).all()

