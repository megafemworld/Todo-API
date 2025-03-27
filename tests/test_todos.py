import pytest
from src.app import create_app
from src.infrastructure.database import Base, engine

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    Base.metadata.create_all(bind=engine)
    with app.test_client() as client:
        yield client

def test_create_todo(client):
    response = client.post('/api/v1/todos', json= {'content': 'Test Todo'})
    assert response.status_code == 201
    assert 'id' in response.json
    
def test_get_todos(client):
    response = client.get('/api/v1/todos')
    assert response.status_code == 200
    assert isinstance(response.json, list) 