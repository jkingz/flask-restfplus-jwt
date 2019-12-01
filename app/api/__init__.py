""" API Blueprint Application """

from flask import Blueprint, current_app
from flask_restplus import Api
# from flask_restful import Api

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api_rest = Api(api_bp, 
        version="1.0",
        title="API",
        description="The api blue print",
        default="API",
        default_label="API information"
        )


@api_bp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

# Import resources to ensure view is registered
from .resources import * # NOQA
