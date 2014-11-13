from . import db
from datetime import datetime

class DietEntry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime)
    creation_date = db.Column(db.DateTime)
    title = db.Column(db.String(120))
    value = db.Column(db.Integer)

    def __init__(self, title, value, timestamp=None):
        self.title = title
        self.value = value
        self.timestamp = timestamp or datetime.now()
        self.creation_date = datetime.now()

    def __repr__(self):
        return '<DietEntry {0} {1} {2} {3}>'.format(self.title, self.value, self.timestamp, self.creation_date)


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))
    birthday = db.Column(db.DateTime)
    height = db.Column(db.Integer)

    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height

    def __repr__(self):
        return '<Profile {0} {1} {2}>'.format(self.name, self.birthday, self.height)
