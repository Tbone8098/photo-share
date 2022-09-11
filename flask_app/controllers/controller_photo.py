from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.config.helper import upload_photo

from flask_app.models import model_photo
from flask_app.models.albums import model_album_has_photos

import base64


@app.route('/photo/new')
def photo_new():
    return render_template('photo_new.html')


@app.route('/photo/create', methods=['POST'])
def photo_create():

    data = {
        'description': request.form['description']
    }
    if request.files['file']:
        data['url'] = upload_photo(request.files['file'])
    else:
        data['url'] = request.form['url'],

    album_id = request.form['album_id']
    photo_id = model_photo.Photo.create(**data)
    data = {
        'photo_id': photo_id,
        'album_id': album_id
    }
    model_album_has_photos.AlbumsHasPhotos.create(**data)
    return redirect(f'/album/{album_id}')


@app.route('/photo/<int:id>')
def photo_show(id):
    return render_template('photo_show.html')


@app.route('/photo/<int:id>/edit')
def photo_edit(id):
    return render_template('photo_edit.html')


@app.route('/photo/<int:id>/update', methods=['POST'])
def photo_update(id):
    return redirect('/')


@app.route('/photo/<int:id>/delete')
def photo_delete(id):
    return redirect('/')
