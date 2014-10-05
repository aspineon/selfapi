from . import con
from mongokit import *
from datetime import datetime


class DietEntry(Document):
    structure = {
        'timestamp': datetime,
        'created_at': datetime,
        'title': unicode,
        'value': int
    }

    use_dot_notation = True
    required_fields = ['timestamp', 'title', 'value']
    default_values = {'timestamp': datetime.now, 'created_at': datetime.now}


class Profile(Document):
    structure = {
        'name': unicode,
        'birthday': datetime,
        'height': int
    }


con.register([DietEntry])
