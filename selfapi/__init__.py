from flask import Flask
from mongokit import Connection, Document

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

con = Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])

import views
