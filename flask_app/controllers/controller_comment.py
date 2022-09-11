from flask_app import app
from flask import render_template, redirect, session, request, jsonify

from flask_app.models import model_comment, model_user

@app.route('/comment/new')          
def comment_new():
    return render_template('comment_new.html')

@app.route('/api/comment/create', methods=['POST'])          
def api_comment_create():
    errors = model_comment.Comment.api_validator(request.form)
    if len(errors):
        photo_id = request.form['photo_id']
        msg = {
            'status': 404,
            'photo_id': photo_id,
            'errors': errors
        }
        return jsonify(msg)
    data = {
        **request.form,
        'user_id': session['uuid']
    }
    comment_id = model_comment.Comment.create(**data)

    user = model_user.User.get_one(id=session['uuid'])
    comment = model_comment.Comment.get_one(id=comment_id)
    msg = {
        'status': 200,
        'photo': {
            'id': request.form['photo_id']
        },
        'user': {
            'fullname': user.fullname
        },
        'comment': {
            'id': comment.id,
            'content': comment.content,
            'updated_at': comment.updated_at
        }
    }
    return jsonify(msg)
    # album_id = session['album_id']
    # return redirect(f'/album/{album_id}')

@app.route('/comment/<int:id>')          
def comment_show(id):
    return render_template('comment_show.html')

@app.route('/comment/<int:id>/edit')          
def comment_edit(id):
    return render_template('comment_edit.html')

@app.route('/comment/<int:id>/update', methods=['POST'])          
def comment_update(id):
    return redirect('/')

@app.route('/api/comment/<int:id>/delete')          
def api_comment_delete(id):
    album_id = session['album_id']
    comment = model_comment.Comment.get_one(id=id)
    if comment.user_id != session['uuid']:
        return redirect(f'/album/{album_id}')

    model_comment.Comment.delete_one(id=id)
    return jsonify(msg = 'success')
    # return redirect(f'/album/{album_id}')
