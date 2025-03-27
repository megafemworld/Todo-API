from flask_jwt_extended import JWTManager
from datetime import timedelta

jwt = JWTManager()

def configure_jwt(app):
    app.config["JWT_SERECT_KEY"] = "super_secrect"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    jwt.init_app(app)