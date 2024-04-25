from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_add_to_cart_and_checkout():
    response = client.post("/cart/add-item", json={"product_id": 1, "quantity": 2})
    print(response.json())
    assert response.status_code == 200

    response = client.post("/checkout")
    print(response.json())
    assert response.status_code == 200
    assert response.json()["discount"] == 0  # No discount on the first order
