# app/__init__.py

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
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
