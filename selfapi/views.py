from flask import render_template, request
from . import app
from models import *
from forms import DietForm


@app.route('/')
def index():
    collection = con['selfapi'].diet
    entries = list(collection.DietEntry.find())
    return render_template('list.html', entries=entries)

@app.route('/diet', methods = ['GET', 'POST'])
def diet_form():
    form = DietForm()
    return render_template('diet_form.html', form = form)