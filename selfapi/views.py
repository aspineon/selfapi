from flask import render_template, request
from . import app, api
from models import *

@app.route('/')
def index():
    collection = con['selfapi'].diet
    entries = list(collection.DietEntry.find())
    return render_template('list.html', entries=entries)

@app.route('/diet', methods = ['GET'])
def diet_form():
    return render_template('diet_form.html')