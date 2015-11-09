from app import db
from datetime import datetime

class Location(db.Model):
    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, id, name):
        self.name = name

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    destination_id = db.Column(db.Integer, db.ForeignKey(location.id))

    location = db.relationship('Location', foreign_keys=destination_id)

    def __init__(self, first_name, last_name, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location

class Group(db.Model):
    __tablename__ = "group"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    final_destination_id = db.Column(db.Integer, db.ForeignKey(location.id))

    location = db.relationship('Location', foreign_keys=final_destination_id)

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Walker(db.Model):
    __tablename__ = "walker"
    id = db.Column(db.Integer, db.ForeignKey(user.id))
    origin_id = db.Column(db.Integer, db.ForeignKey(location.id))
    target_id = db.Column(db.Integer, db.ForeignKey(location.id))
    start_time = db.Column(db.DateTime)
    group_id = db.Column(db.Integer, db.ForeignKey(group.id))

    user = db.relationship('User', foreign_keys=id)
    location = db.relationship('Location', foreign_keys=origin_id)
    location = db.relationship('Location', foreign_keys=target_id)
    group = db.relationship('Group', foreign_keys=group_id)

    def __init__(self, start_time, user, location, location, group):
        start_time = datetime.utcnow()
        self.start_time = start_time
        self.user = user
        self.location = location
        self.location = location
        self.group = group
