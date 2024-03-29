"""
REST API Resource Routing
https://flask-restful.readthedocs.io/
"""
from flask_restplus import Resource, reqparse
# from flask_restful import Resource
from flask_jwt_extended import (
        create_access_token, 
        create_refresh_token, 
        jwt_required, 
        jwt_refresh_token_required, 
        get_jwt_identity, get_raw_jwt
    )

from . import api_rest
from app.models import UserModel, RevokedTokenModel

parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)


@api_rest.route('/registration')
class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {
                'message': f"User {data['username']} already exists."
            }
        new_user = UserModel(
            username = data['username'],
            password = UserModel.generate_hash(data['password'])
        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return{
                'message': f"User {data['username']} was created",
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except:
            return {'message': f"something went wrong"}, 500


@api_rest.route('/login')
class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])
        if not current_user:
            return{
                'message': f"User {data['username']} doesn\'t exist'"
            }
        
        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity = data['username'])
            refresh_token = create_refresh_token(identity = data['username'])
            return{
                'message': f"Logged in as {current_user.username}",
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return{
                'message': f"Wrong credentials"
            }


@api_rest.route('/logout/access')
class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': f"Access token has been revoked"}
        except:
            return {'message': 'Something went wrong'}, 500


@api_rest.route('/logout/refresh')
class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


@api_rest.route('/token/refresh')
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}


@api_rest.route('/users')
class allUsers(Resource):
    def get(self):
        return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()


@api_rest.route('/secret')
class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }
