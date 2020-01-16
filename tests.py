from starlette.testclient import TestClient

from main import app

client = TestClient(app)

def test_main_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_main_response_json():
    response = client.get("/")
    assert response.json() == {"hello": "world"}

def test_todo_list():
    response = client.get("/todo")
    assert len(response.json()) == 3