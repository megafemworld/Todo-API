from flask_jwt_extended import create_access_token
from flask import Blueprint, request, jsonify
from src.domain.models import User
from src.infrastructure.database import get_db

auth_bp = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing 'email' or 'password' field"}), 400
    db = next(get_db())
    if db.query(User).filter_by(email=data['email']).first():
        return jsonify({"error": "Email already in use"}), 400
    user = User(email=data['email'])
    user.set_password(data['password'])
    db.add(user)
    db.commit()
    return jsonify({"message": "User created"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    db = next(get_db())
    user = db.query(User).filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401