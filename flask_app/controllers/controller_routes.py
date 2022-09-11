from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.config.helper import login_required
from flask_app.models import model_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('pages/dashboard/main.html')


@app.route('/<path:path>')
def catch_all(path):
    return 'page not found'