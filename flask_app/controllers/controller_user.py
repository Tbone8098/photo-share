from flask_app import app, bcrypt
from flask import render_template, redirect, session, request

from flask_app.models import model_user

@app.route('/user/new')          
def user_new():
    return render_template('user_new.html')

@app.route('/user/logout')          
def user_logout():
    del session['uuid']
    return redirect('/')

@app.route('/user/process_login', methods=['POST'])          
def user_process_login():
    potential_user = model_user.User.get_one(email=request.form['email'])
    if not potential_user:
        print("user not found")
        return redirect('/')
    if not bcrypt.check_password_hash(potential_user.pw, request.form['pw']):
        print("Bad Password")
        return redirect('/')
    session['uuid'] = potential_user.id
    return redirect('/dashboard')

@app.route('/user/create', methods=['POST'])          
def user_create():
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw': hash_pw
    }
    del data['confirm_pw']
    user_id = model_user.User.create(**data)
    session['uuid'] = user_id
    return redirect('/dashboard')

@app.route('/user/<int:id>')          
def user_show(id):
    return render_template('user_show.html')

@app.route('/user/<int:id>/edit')          
def user_edit(id):
    return render_template('user_edit.html')

@app.route('/user/<int:id>/update', methods=['POST'])          
def user_update(id):
    return redirect('/')

@app.route('/user/<int:id>/delete')          
def user_delete(id):
    return redirect('/')
