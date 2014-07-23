from flask import render_template, redirect, url_for

from . import app

@app.route('/foo')
def index():
	return 'Hello world!'