from flask import render_template, request
from . import app, api, db
from selfapi import DietEntry, Profile
from datetime import date, timedelta

@app.route('/')
def index():
    entries = list(DietEntry.query.all())
    return render_template('list.html', entries=entries)

@app.route('/diet', methods = ['GET'])
def diet_form():
    entries = list(DietEntry.query.all())
    return render_template('diet.html', entries = entries)

@app.route('/diet/today', methods = ['GET'])
def diet_form_today():
    today = date.today()
    tomorrow = date.today() + timedelta(days=1)
    entries = list(DietEntry.query.filter(DietEntry.timestamp.between(today, tomorrow)))
    return render_template('diet.html', entries = entries)

@app.route('/profile', methods = ['GET'])
def profile():
    profile = Profile.query.first()
    return render_template('profile.html', profile=profile)