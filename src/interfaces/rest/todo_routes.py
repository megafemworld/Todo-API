from flask import Blueprint, request, jsonify
from src.domain.models import Todo
from src.infrastructure.database import get_db

bp = Blueprint('todos', __name__, url_prefix='/api/v1/todos')

@bp.route('', method=['POST'])
def create_todo():
    data = request.get_json()
    if not data or 'content' not in data:
        return jsonify({"error": "Misisng 'content' field"}), 400
    
    db = next(get_db())
    new_todo = Todo(content=data['content'])
    db.add(new_todo)
    db.commit()
    return jsonify(new_todo.to_dict()), 201

@bp.route('', method=['GET'])
def get_todos():
    db = next(get_db())
    todos = db.query(Todo).all()
    return jsonify([todo.to_dict() for todo in todos])