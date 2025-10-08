
from app import app

def test_home_message():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data.decode() == "Hello, CI/CD World4!"

