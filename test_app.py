import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create(client):
    response = client.post('/strings', json={"string": "hello"})
    assert response.status_code == 201

def test_create_duplicate(client):
    client.post('/strings', json={"string": "hello"})
    response = client.post('/strings', json={"string": "hello"})
    assert response.status_code == 400

def test_read(client):
    client.post('/strings', json={"string": "test"})
    response = client.get('/strings')
    assert response.status_code == 200
    assert "test" in response.json['data']

def test_update(client):
    client.post('/strings', json={"string": "test"})
    response = client.put('/strings/test', json={"new_string": "updated"})
    assert response.status_code == 200

def test_delete(client):
    client.post('/strings', json={"string": "to_delete"})
    response = client.delete('/strings/to_delete')
    assert response.status_code == 200
