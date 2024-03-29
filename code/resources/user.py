
from flask_restful import Resource, reqparse
from models.user_model import UserModel

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
        user = UserModel(**data)
        if UserModel.find_by_username(data['username']):
            return {'message': 'A user with that username already exist'}, 400

        user.save_user_to_database()
        return {'message' : 'User created succesfully'}