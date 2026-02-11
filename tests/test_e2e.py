# tests/test_e2e.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_low_stock_e2e():
    product = {"nombre": "Test", "precio": 50.0, "categoria": "tech", "stock": 3}
    response = client.post("/products", json=product)
    assert response.status_code == 200
    assert response.json() == product

    response_low = client.get("/products/low-stock")
    assert response_low.status_code == 200
    assert len(response_low.json()) == 1
