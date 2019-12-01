import os
from flask import Flask, current_app, send_file
from flask_jwt_extended import JWTManager

from .api import api_bp
from .client import client_bp
from .extensions import db

app = Flask(__name__, static_folder='../dist/static')
app.register_blueprint(api_bp)
# app.register_blueprint(client_bp)

@app.before_first_request
def create_tables():
    db.create_all()

from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))

jwt = JWTManager(app)

@app.route('/')
def index_client():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)
