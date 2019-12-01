"""
REST API Resource Routing
https://flask-restful.readthedocs.io/
"""
from flask_restplus import Resource, reqparse
# from flask_restful import Resource

from . import api_rest


parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)


@api_rest.route('/registration')
class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        return data


@api_rest.route('/login')
class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        return data


@api_rest.route('/logout/access')
class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'logout'}


@api_rest.route('/logout/refresh')
class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'logout refresh'}


@api_rest.route('/token/refresh')
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


@api_rest.route('/users')
class allUsers(Resource):
    def get(sefl):
        return {'message': 'Hello users'}

    def post(sefl):
        return {'message': 'delete users'}

@api_rest.route('/secret')
class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }
