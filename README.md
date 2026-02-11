📦 Instalación
1. Clonar el repositorio
bash
git clone https://github.com/Abraham-HUB-777/fastapi-products.git
cd fastapi-products
2. Crear entorno virtual e instalar dependencias
bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
▶️ Ejecución
Levantar el servidor con Uvicorn:

bash
uvicorn app.main:app --reload
La API estará disponible en:

👉 http://127.0.0.1:8000

📚 Documentación interactiva
FastAPI genera documentación automática:

Swagger UI: http://127.0.0.1:8000/docs  
Interfaz interactiva para probar los endpoints.

ReDoc: http://127.0.0.1:8000/redoc  
Documentación detallada con ejemplos de request y response.

🔗 Endpoints disponibles
Método	Ruta	Descripción
GET	/products	Obtener todos los productos
POST	/products	Crear un producto
GET	/products/{id}	Obtener un producto por ID
PUT	/products/{id}	Actualizar un producto por ID
DELETE	/products/{id}	Eliminar un producto por ID
🧪 Ejemplos de uso con curl
➤ Crear un producto
bash
curl -X POST http://127.0.0.1:8000/products \
-H "Content-Type: application/json" \
-d '{"nombre": "Laptop", "precio": 1200.0, "categoria": "tech", "stock": 5}'
➤ Obtener todos los productos
bash
curl http://127.0.0.1:8000/products
➤ Actualizar un producto
bash
curl -X PUT http://127.0.0.1:8000/products/1 \
-H "Content-Type: application/json" \
-d '{"nombre": "Laptop Pro", "precio": 1500.0, "categoria": "tech", "stock": 4}'
➤ Eliminar un producto
bash
curl -X DELETE http://127.0.0.1:8000/products/1
🧪 Testing
Ejecutar los tests:

bash
pytest
Si todo está correcto, los tests deberían pasar sin problemas.

🤝 Cómo contribuir
Haz un fork del repositorio.

Crea una nueva rama:

bash
git checkout -b mi-nueva-funcionalidad
Realiza tus cambios y commitea:

bash
git commit -m "Añadida nueva funcionalidad X"
Sube tu rama:

bash
git push origin mi-nueva-funcionalidad
Abre un Pull Request en GitHub.

📬 Contacto
Autor: Abraham-HUB-777
GitHub: https://github.com/Abraham-HUB-777  
Email: abraham.iessanmamde

📄 Licencia
Este proyecto está bajo la MIT License.