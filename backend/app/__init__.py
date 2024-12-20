# app/__init__.py
from flask import Flask
from flask_cors import CORS
from app.api.v1.address.routes import address_bp

def register_blueprints(app):
    app.register_blueprint(address_bp, url_prefix='/api/v1/address')


def create_app():
    app = Flask(__name__)

    # Load configuration from a file or set configuration options here
    app.config.from_pyfile('config.py')

    # Enable CORS for all origins
    CORS(app, origins="*")

    # Register blueprints
    register_blueprints(app)

    print("App running successfully")

    return app