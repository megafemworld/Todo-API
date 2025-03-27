from flask import Blueprint, request, jsonify
from domain.models import Todo
from src.infrastructure.database import get_db
from src.infrastructure.caching import cache

bp = Blueprint('todos', __name__, url_prefix='/api/v1/todos')

@bp.route('', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or 'content' not in data:
        return jsonify({"error": "Misisng 'content' field"}), 400
    
    db = next(get_db())
    new_todo = Todo(content=data['content'])
    db.add(new_todo)
    db.commit()
    return jsonify(new_todo.to_dict()), 201

@bp.route('', methods=['GET'])
@cache.cached(timeout=60, query_string=True)
def get_todos():
    db = next(get_db())
    todos = db.query(Todo).all()
    return jsonify([todo.to_dict() for todo in todos])