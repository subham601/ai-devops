from fastapi.testclient import TestClient

from app.main import app


def test_login_and_cart_flow():
    client = TestClient(app)

    # login
    login_resp = client.post(
        "/api/auth/login",
        json={"email": "demo@example.com", "password": "demo123"},
    )
    assert login_resp.status_code == 200
    token = login_resp.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    # add to cart
    add_resp = client.post(
        "/api/cart/items",
        json={"product_id": 1, "quantity": 2},
        headers=headers,
    )
    assert add_resp.status_code == 200
    assert add_resp.json()["ok"] is True

    # get cart
    cart_resp = client.get("/api/cart", headers=headers)
    assert cart_resp.status_code == 200
    cart = cart_resp.json()
    assert "items" in cart
    assert cart["items"]
    assert cart["items"][0]["product_id"] == 1
    assert cart["items"][0]["quantity"] == 2

