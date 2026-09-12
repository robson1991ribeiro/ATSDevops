from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_windows():
    response = client.get("/windows")
    assert response.status_code == 200

def test_rede():
    response = client.get("/rede")
    assert response.status_code == 200