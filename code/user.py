import sqlite3
from flask_restful import Resource, reqparse
from database import selectItem, insertItem

class User:

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        row = selectItem("SELECT * FROM users WHERE username=?", username)
        return cls(*row) if row else None

    @classmethod
    def find_by_id(cls,_id):
        row = selectItem("SELECT * FROM users WHERE id=?", _id)
        return cls(*row) if row else None


class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required = True,
        help = "This field cannot be left blank!"
    )

    parser.add_argument('password',
        type = str,
        required = True,
        help = "This field cannot be left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'A user with that username already exist'}, 400

        insertItem("INSERT INTO users VALUES (NULL, ?, ?)", (data['username'], data['password']))
        return {'message' : 'User created succesfully'}

