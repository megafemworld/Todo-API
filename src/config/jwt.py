from flask_jwt_extended import JWTManager

jwt = JWTManager()

def configure_jwt(app):
    app.config["JWT_SERECT_KEY"] = "super_secrect"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    jwt.init_app(app)