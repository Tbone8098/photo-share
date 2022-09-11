from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base
from flask_app import DATABASE_SCHEMA
import re

class Comment(model_base.base_model):
    table = 'comments'
    def __init__(self, data):
        super().__init__(data)
        self.photo_id = data['photo_id']
        self.user_id = data['user_id']
        self.content = data['content']

    @staticmethod
    def api_validator(data):
        errors = {}

        if len(data['content']) < 1:
            errors['err_content'] = 'Content is required'

        return errors