# tests/test_unit_service.py
from app.service import ProductService

def test_create_and_low_stock():
    service = ProductService()
    product = {"nombre": "Test", "precio": 50.0, "categoria": "tech", "stock": 3}
    
    created = service.create_product(product)
    assert created == product

    low = service.low_stock()
    assert len(low) == 1
