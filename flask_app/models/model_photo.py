from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_comment, model_user
from flask_app import DATABASE_SCHEMA
import re

class Photo(model_base.base_model):
    table = 'Photos'
    def __init__(self, data):
        super().__init__(data)
        self.url = data['url']
        self.description = data['description']
        self.photo_x = data['photo_x']
        self.photo_y = data['photo_y']
        
    @property
    def all_comments(self):
        query = f"SELECT * FROM comments JOIN photos ON comments.photo_id = photos.id JOIN users ON comments.user_id = users.id WHERE photos.id = {self.id}"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if not results:
            return []
        all_comments = []
        for dict in results:
            comment = model_comment.Comment(dict)
            user_data = {
                **dict,
                'id': dict['users.id'],
                'created_at': dict['users.created_at'],
                'updated_at': dict['users.updated_at'],
            }
            comment.maker = model_user.User(user_data)
            all_comments.append(comment)
        return all_comments