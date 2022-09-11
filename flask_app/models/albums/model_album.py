from this import d
from unittest import result
from xml.etree.ElementTree import QName
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_photo, model_user
from flask_app import DATABASE_SCHEMA

class Album(model_base.base_model):
    table = 'albums'
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']
        self.code = data['code']
        self.cover_url = data['cover_url']
        self.cover_x = data['cover_x']
        self.cover_y = data['cover_y']
        self.creator_id = data['creator_id']

    @property
    def all_members(self):
        query = f"SELECT * FROM users JOIN albums_has_users ON albums_has_users.user_id = users.id WHERE albums_has_users.album_id = {self.id}"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if not results:
            return []
        all_users = []
        for dict in results:
            all_users.append( model_user.User(dict) )
        return all_users

    @property
    def all_photos(self):
        query = f"SELECT * FROM photos JOIN albums_has_photos ON photos.id = albums_has_photos.photo_id WHERE albums_has_photos.album_id = {self.id};"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if not results:
            return []
        all_photos = []
        for dict in results:
            all_photos.append( model_photo.Photo(dict) )
        return all_photos

    @classmethod
    def get_all(cls, data:dict) -> list:
        query = "SELECT * FROM albums JOIN albums_has_users ON albums.id = albums_has_users.album_id WHERE albums_has_users.user_id = %(id)s;"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        if not results:
            return []
        all_albums = []
        for dict in results:
            all_albums.append( cls(dict) )
        return all_albums
