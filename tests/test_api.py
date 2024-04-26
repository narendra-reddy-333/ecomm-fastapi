from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is in main.py

client = TestClient(app)


def test_add_item_to_cart():
    item_data = {"product_id": 1, "quantity": 2, "price": 9.99}
    response = client.post("/api/cart/items", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Item added to cart"}


def test_checkout_empty_cart():
    response = client.post("/api/checkout")
    assert response.status_code == 400
    assert response.json()["detail"] == "Cart is empty"


def test_checkout_with_items():
    test_add_item_to_cart()
    response = client.post("/api/checkout")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "total_price" in data


def test_generate_discount_code():
    response = client.post("/api/admin/discount")
    assert response.status_code == 200
    data = response.json()
    assert "code" in data
    assert len(data["code"]) > 0


def test_get_stats():
    response = client.get("/api/admin/stats")
    assert response.status_code == 200
    data = response.json()
    assert "total_items" in data
    assert "total_purchase_amount" in data
    assert "discount_codes" in data
    assert "total_discount_amount" in data

