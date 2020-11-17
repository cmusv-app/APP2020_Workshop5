from flask_restful import fields, marshal_with, reqparse, Resource
from services.UserService import *
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

user_fields = {
    'email': fields.String,
}

post_parser = reqparse.RequestParser()
post_parser.add_argument('email', type=str)


class Users(Resource):

    @marshal_with(user_fields, envelope='data')
    @jwt_required
    def get(self, u_id):
        the_email_identity = get_jwt_identity()
        returned_user = find_user_by_id(u_id)
        if the_email_identity == returned_user.email:
            return returned_user
        return 401, "bad credentials"

