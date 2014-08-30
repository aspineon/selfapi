from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, IntegerField, DateTimeField
from wtforms.validators import Required
import datetime

class DietForm(Form):
  title = TextField('title', validators = [Required()])
  value = IntegerField('value', validators = [Required()])
  timestamp = DateTimeField('timestamp', default = datetime.datetime.now(), validators = [Required()])

