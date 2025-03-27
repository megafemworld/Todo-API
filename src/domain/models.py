from sqlalchemy import Column, Integer, String
from src.infrastructure.database import Base
from werkzeug.security import generate_password_hash, check_password_hash

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(200), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content
        }

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)