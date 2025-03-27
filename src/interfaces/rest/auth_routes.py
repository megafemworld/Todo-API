from flask_jwt_extended import create_access_token 

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(email=data['email'])
    user.set_password(data['password'])
    db.add(user)
    deb.commit()
    return jsonify({"message": "User created"}), 201

