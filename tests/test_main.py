import sys
from pathlib import Path
from unittest.mock import patch

sys.path.append(str(Path(__file__).resolve().parent.parent))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_windows_status_code():
    response = client.get("/windows")
    assert response.status_code == 200


def test_rede_status_code():
    response = client.get("/rede")
    assert response.status_code == 200


def test_home_template():
    with patch("main.templates.TemplateResponse") as mock_template:
        client.get("/")
        assert mock_template.called
        assert mock_template.call_args.kwargs["name"] == "index.html"


def test_windows_template():
    with patch("main.templates.TemplateResponse") as mock_template:
        client.get("/windows")
        assert mock_template.called
        assert mock_template.call_args.kwargs["name"] == "windows.html"


def test_rede_template():
    with patch("main.templates.TemplateResponse") as mock_template:
        client.get("/rede")
        assert mock_template.called
        assert mock_template.call_args.kwargs["name"] == "rede.html"


def test_rota_inexistente():
    response = client.get("/abc")
    assert response.status_code == 404