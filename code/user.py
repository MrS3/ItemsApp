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
        return cls(*selectItem("SELECT * FROM users WHERE username=?", username))

    @classmethod
    def find_by_id(cls,_id):
        return cls(*selectItem("SELECT * FROM users WHERE id=?", _id))


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

        connection = sqlite3.connect('data.db')
        currsor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        result = currsor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()
        return {'message' : 'User created succesfully'}

