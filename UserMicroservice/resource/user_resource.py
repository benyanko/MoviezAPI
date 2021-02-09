from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity, JWT
from models.user_model import UserModel
from flask import request
import requests



class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )
    parser.add_argument('access',
                        type=int,
                        required=True,
                        choices=[1, 2],
                        help='access value should be 1 or 2'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created"}, 201


class UserLoggedIn(Resource):
    @jwt_required()
    def get(self):
        _id = current_identity.__str__()
        user = UserModel.find_by_id(_id)

        if user:
            #return {"id": user.id, "access": user.access}
            return user.json(), 200
