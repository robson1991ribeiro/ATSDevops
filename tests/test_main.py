import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from main import app
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


def test_home_html():
    response = client.get("/")
    assert "text/html" in response.headers["content-type"]


def test_windows_html():
    response = client.get("/windows")
    assert "text/html" in response.headers["content-type"]


def test_rota_inexistente():
    response = client.get("/pagina-nao-existe")
    assert response.status_code == 404