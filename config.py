# config.py
# This file stores configuration variables for the Flask app.
# Using a class-based config makes it easy to have multiple
# configurations (e.g., for Development, Testing, Production).

import os

class Config:
    """
    Main application configuration.
    """
    
    # SECRET_KEY is crucial for security.
    # It's used for session management, signing cookies,
    # and protecting against Cross-Site Request Forgery (CSRF).
    # We try to get it from an environment variable first (for production)
    # and use a default value for development if it's not set.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-hard-to-guess-secret-key'