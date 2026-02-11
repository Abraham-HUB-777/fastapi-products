# app/main.py
from fastapi import FastAPI
from app.service import ProductService

app = FastAPI()
service = ProductService()

@app.post("/products")
def create_product(product: dict):
    return service.create_product(product)

@app.get("/products")
def list_products():
    return service.list_products()

@app.get("/products/low-stock")
def low_stock(threshold: int = 5):
    return service.low_stock(threshold)
