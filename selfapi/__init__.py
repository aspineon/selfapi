from flask import Flask
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy

# TODO figure out how to do instance deployent for heroku
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
#app.config.from_pyfile('config.py')

api = Api(app)

db = SQLAlchemy(app)

from models import DietEntry, Profile
import api
import views
