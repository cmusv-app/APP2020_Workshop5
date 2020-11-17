from flask import jsonify, make_response
from flask_restful import fields, marshal_with, reqparse, Resource
from hashlib import md5

from services.UserService import *
from flask_jwt_extended import create_access_token

reg_parser = reqparse.RequestParser()
reg_parser.add_argument('email', type=str)
reg_parser.add_argument('password', type=str)


class UserRegistration(Resource):

    def get(self, user_id):
        return True

    def post(self):
        args = reg_parser.parse_args()
        found_user = find_user_by_email(args.email)
        if found_user:
            return "Account with this email already exists", 400

        hasher = md5()
        password = args.password.encode('utf-8')
        hasher.update(password)
        password_hash = hasher.hexdigest()
        create_user(args.email, password_hash)
        access_token = create_access_token(identity=args.email)
        return make_response(jsonify(access_token=access_token), 200)

    def put(self):
        return True


