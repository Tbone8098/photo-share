from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app import DATABASE_SCHEMA

class AlbumHasUser(model_base.base_model):
    table = 'albums_has_users'
    def __init__(self, data):
        super().__init__(data)
