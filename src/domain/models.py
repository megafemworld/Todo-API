from sqlalchemy import Column, Integer, String
from src.infrastructure.database import Base

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(200), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content
        }