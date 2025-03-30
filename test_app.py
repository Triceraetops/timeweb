import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as app_client:
        yield app_client

def testtime(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"20" in response.data 

def testcolor(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"color: pink;" in response.data 
