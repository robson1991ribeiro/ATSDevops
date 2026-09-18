import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.main import app
from fastapi.testclient import TestClient

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

def test_home_content_type():
    response = client.get("/")
    assert response.headers["content-type"].startswith("text/html")

def test_rota_inexistente():
    response = client.get("/inexistente")
    assert response.status_code == 404