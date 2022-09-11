from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app import DATABASE_SCHEMA
import re

class AlbumsHasPhotos(model_base.base_model):
    table = 'albums_has_photos'
    def __init__(self, data):
        super().__init__(data)
        self.photo_id = data['photo_id']
        self.album_id = data['album_id']