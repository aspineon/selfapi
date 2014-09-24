from flask import Flask
from mongokit import Connection
from flask.ext.restful import Api

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

api = Api(app)

con = Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])

import api
import views