from flask import Flask, jsonify
from infrastructure.database import engine, Base
from config.settings import settings
from interfaces.rest import todo_routes, auth_routes

def create_app():
    app = Flask(__name__)
    register_error_handler(app)
    
    # Initialize database
    if settings.ENVIRONMENT != 'test':
        Base.metadata.create_all(bind=engine)
    
    # Register routes
    app.register_blueprint(todo_routes.bp)
    app.register_blueprint(auth_routes.auth_bp)
    
    return app

def handle_bad_request(e):
    return jsonify({"error": "Bad request", "details": str(e)}), 400

def handle_not_found(e):
    return jsonify({"error": "Resource not found"}), 400

def register_error_handler(app):
    app.register_error_handler(400, handle_bad_request)
    app.register_error_handler(404, handle_not_found)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)