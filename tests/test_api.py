from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_ask_endpoint():

    response = client.get(
        "/api/v1/ask",
        params={"question": "What is FastAPI?"}
    )

    assert response.status_code == 200