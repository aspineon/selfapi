from . import con
from mongokit import *
import datetime


class DietEntry(Document):
    structure = {
        'timestamp': datetime.datetime,
        'created_at': datetime.datetime,
        'title': unicode,
        'value': int
    }

    use_dot_notation = True

    required_fields = ['timestamp', 'title', 'value']
    default_values = {'timestamp': datetime.datetime.now, 'created_at': datetime.datetime.now}


con.register([DietEntry])
