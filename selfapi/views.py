from flask import render_template, request
from . import app, api, db
from models import *

@app.route('/')
def index():
    entries = list(db.diet.DietEntry.find())
    return render_template('list.html', entries=entries)

@app.route('/diet', methods = ['GET'])
def diet_form():
    return render_template('diet_form.html')

@app.route('/profile', methods = ['GET'])
def profile():
    profile = db.profile.Profile.find_one()
    print(profile)
    return render_template('profile.html', profile=profile)