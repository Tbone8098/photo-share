from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.config.helper import generate_code

from flask_app.models.albums import model_album, model_album_has_user
from flask_app.models import model_user

@app.route('/albums')
def albums_all():
    context = {
        'all_albums': model_album.Album.get_all({'id': session['uuid']})
    }
    return render_template('/pages/albums/main.html', **context)

@app.route('/album/new')          
def album_new():
    return render_template('album_new.html')

@app.route('/album/create', methods=['POST'])          
def album_create():
    data = {
        'name': request.form['name']
    }

    # create code
    code = generate_code(10)
    while model_album.Album.get_one(code=code):
        code = generate_code(10)

    data['code'] = code
    data['creator_id'] = session['uuid']

    # check to see if uploading a photo or sending a URL
    if request.form['cover_url']:
        data['cover_url'] = request.form['cover_url']
    else:
        #TODO connect to imgbb and upload given photo
        pass

    # create album
    album_id = model_album.Album.create(**data)

    # create albumhasuser
    data = {
        'album_id': album_id,
        'user_id': session['uuid'],
        'access_level': 3
    }
    model_album_has_user.AlbumHasUser.create(**data)
    return redirect('/albums')

@app.route('/album/<int:id>/add_member', methods=['post'])
def add_member(id):
    member = model_user.User.get_one(email=request.form['email'])
    if not member:
        return redirect(f'/album/{id}/share')
    data = {
        'album_id': id,
        'user_id': member.id
    }
    model_album_has_user.AlbumHasUser.create(**data)
    return redirect(f'/album/{id}/share')

@app.route('/album/<int:id>')
@app.route('/album/<int:id>/share')
@app.route('/album/<int:id>/share/emails')
def album_show(id):
    session['album_id'] = id
    context = {
        'album': model_album.Album.get_one(id=id)
    }
    return render_template('pages/albums/show.html', **context)

@app.route('/album/<int:id>/edit')          
def album_edit(id):
    return render_template('album_edit.html')

@app.route('/album/<int:id>/update', methods=['POST'])          
def album_update(id):
    return redirect('/')

@app.route('/album/<int:id>/delete')          
def album_delete(id):
    model_album_has_user.AlbumHasUser.delete_one(album_id = id)
    model_album.Album.delete_one(id=id)
    return redirect('/albums')
