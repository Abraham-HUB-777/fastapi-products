# app/service.py

class ProductService:
    def __init__(self):
        self.products = []

    def create_product(self, product):
        self.products.append(product)
        return product

    def list_products(self):
        return self.products

    def low_stock(self, threshold=5):
        return [p for p in self.products if p.get("stock", 0) < threshold]
