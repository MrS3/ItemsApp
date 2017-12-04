import sqlite3
from flask_restful import Resource, reqparse
from database import selectItem, manageItem
from user_model import UserModel

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

        if UserModel.find_by_username(data['username']):
            return {'message': 'A user with that username already exist'}, 400

        insertItem("INSERT INTO users VALUES (NULL, ?, ?)", (data['username'], data['password']))
        return {'message' : 'User created succesfully'}

