from fastapi.testclient import TestClient

from app.main import app


def test_products_endpoint_returns_items():
    client = TestClient(app)
    resp = client.get("/api/products")
    assert resp.status_code == 200
    body = resp.json()
    assert "items" in body
    assert isinstance(body["items"], list)
    assert len(body["items"]) > 0

