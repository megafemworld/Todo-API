from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.domain.models import Todo
from src.infrastructure.database import get_db
from src.infrastructure.caching import cache

bp = Blueprint('todos', __name__, url_prefix='/api/v1/todos')

@bp.route('/', methods=['POST'])
def create_todo():
    current_user = get_jwt_identity()
    data = request.get_json()
    if not data or 'content' not in data:
        return jsonify({"error": "Misisng 'content' field"}), 400
    
    db = next(get_db())
    new_todo = Todo(content=data['content'], user_id=current_user)
    db.add(new_todo)
    db.commit()
    return jsonify(new_todo.to_dict()), 201

@bp.route('', methods=['GET'])
@cache.cached(timeout=60, query_string=True)
@jwt_required()
def get_todos():
    current_user = get_jwt_identity()
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    db = next(get_db())
    todos = db.query(Todo).filter_by(user_id=current_user)\
        .offset((page - 1) * per_page)\
        .limit(per_page)\
        .all()
    return jsonify([todo.to_dict() for todo in todos])