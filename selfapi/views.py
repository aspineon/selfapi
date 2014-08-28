from flask import render_template, redirect, url_for
from . import app, con
from models import *

@app.route('/')
def index():
  collection = con['selfapi'].diet
  entries = list(collection.DietEntry.find())
  #for entry in entries:
   # timestamps.append(entry['timestamp'])
  return render_template('list.html', entries=entries)

@app.route('/add')
def add():
  collection = con['selfapi'].diet
  entry = collection.DietEntry()
  entry['title'] = u'Test Entry'
  entry['value'] = 1000
  entry.save()
  return 'success!'

