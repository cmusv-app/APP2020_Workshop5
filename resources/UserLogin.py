from flask import jsonify, make_response
from flask_restful import reqparse, Resource
from hashlib import md5

from services.UserService import *
from flask_jwt_extended import create_access_token

login_parser = reqparse.RequestParser()
login_parser.add_argument('email', type=str)
login_parser.add_argument('password', type=str)


class UserLogin(Resource):
    def post(self):
        args = login_parser.parse_args()
        found_user = find_user_by_email(args.email)
        if found_user:
            hasher = md5()
            password = args.password.encode('utf-8')
            hasher.update(password)
            password_hash = hasher.hexdigest()

            if password_hash == found_user.password_hash:
                access_token = create_access_token(identity=args.email)
                return make_response(jsonify(access_token=access_token), 200)

        return "No account with these credentials", 401