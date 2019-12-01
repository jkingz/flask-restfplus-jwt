"""
Global flask Application Settings

See `.flaskenv` for default settings.
"""
import os
from flask_cors import CORS


from app import app

class Config(object):
    # If not set fall back to production for safety
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    # Set FLASK_SECRET on your production Environment
    SECRET_KEY = os.getenv('FLASK_SECRET', 'Secret')

    # DATABASE
    #

    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    # if not os.path.exists(DIST_DIR):
    #     raise Exception(
    #         'DIST_DIR not found: {}'.format(DIST_DIR))

app.config.from_object('app.config.Config')
CORS(app)
