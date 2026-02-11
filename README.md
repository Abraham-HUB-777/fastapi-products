# FastAPI Products API

API simple para gestión de productos con FastAPI.  
Permite crear, leer, actualizar y eliminar productos de forma sencilla.

![Python Tests](https://github.com/Abraham-HUB-777/fastapi-products/actions/workflows/python-app.yml/badge.svg)

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Abraham-HUB-777/fastapi-products.git
cd fastapi-products

## Crear un entorno virtual e instalar dependencias:
python -m venv venv

# En Windows
venv\Scripts\activate

# En Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

## Ejecucion

uvicorn app.main:app --reload
La API estará disponible en http://127.0.0.1:8000.

## Endpoints

| Método | Ruta           | Descripción                   |
| ------ | -------------- | ----------------------------- |
| GET    | /products      | Obtener todos los productos   |
| POST   | /products      | Crear un producto             |
| GET    | /products/{id} | Obtener un producto por ID    |
| PUT    | /products/{id} | Actualizar un producto por ID |
| DELETE | /products/{id} | Eliminar un producto por ID   |

Ejemplos de uso con curl

Crear un producto:

curl -X POST http://127.0.0.1:8000/products \
-H "Content-Type: application/json" \
-d '{"nombre": "Laptop", "precio": 1200.0, "categoria": "tech", "stock": 5}'


Obtener todos los productos:

curl http://127.0.0.1:8000/products


Actualizar un producto:

curl -X PUT http://127.0.0.1:8000/products/1 \
-H "Content-Type: application/json" \
-d '{"nombre": "Laptop Pro", "precio": 1500.0, "categoria": "tech", "stock": 4}'


Eliminar un producto:

curl -X DELETE http://127.0.0.1:8000/products/1

Testing

Ejecutar todos los tests unitarios y de integración:

pytest


Todos los tests deberían pasar si la API está funcionando correctamente.

Licencia

MIT License