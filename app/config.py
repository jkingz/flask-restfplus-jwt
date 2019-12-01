"""
Global flask Application Settings

See `.flaskenv` for default settings.
"""
import os
from flask_cors import CORS
from .extensions import db


from app import app

class Config(object):
    # If not set fall back to production for safety
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')

    # DATABASE
    #
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #JWT
    JWT_SECRET_KEY = 'jwt-secret-string'

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    # if not os.path.exists(DIST_DIR):
    #     raise Exception(
    #         'DIST_DIR not found: {}'.format(DIST_DIR))

app.config.from_object('app.config.Config')
db.init_app(app)
CORS(app)
