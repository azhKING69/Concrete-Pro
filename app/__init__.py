# app/__init__.py
# This file turns the 'app' directory into a Python package.
# It also contains the "application factory" function, create_app.

from flask import Flask
from config import Config

def create_app(config_class=Config):
    """
    Application factory pattern.
    Creates and configures an instance of the Flask application.
    """
    
    # Create the Flask app instance
    app = Flask(__name__)
    
    # Load the configuration from the Config object
    app.config.from_object(config_class)

    # --- Register Blueprints ---
    # Blueprints help organize the app into components.
    # We import and register our 'main' blueprint from routes.py.
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # You could initialize other extensions here (e.g., database)
    # db.init_app(app)

    return app