from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {
        "message": "fastapi test on /"
    }


def test_emp():
    response = client.get("/emp")

    assert response.status_code == 200
    assert response.json() == {
        "message": "fastapi test on /emp - hello"
    }


def test_wmp():
    response = client.get("/wmp")

    assert response.status_code == 200
    assert response.json() == {
        "message": "fastapi test on /wmp - world"
    }

