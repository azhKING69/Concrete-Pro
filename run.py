# run.py
# This is the main entry point for the Flask application.
# It imports the create_app function from our 'app' package
# and starts the built-in Flask development server.

from app import create_app

# Create an instance of the Flask application
# using our application factory
app = create_app()

if __name__ == '__main__':
    # This conditional ensures that the server is only run
    # when the script is executed directly (not imported)
    # debug=True will auto-reload the server on code changes
    # and provide detailed error pages.
    # DO NOT use debug=True in production.
    app.run(debug=True)