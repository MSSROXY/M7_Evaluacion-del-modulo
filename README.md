# Mi Tienda - Aplicación Django

Aplicación web para gestionar Productos, Categorías y Etiquetas usando Django. Incluye autenticación de usuarios y una interfaz administrativa.

## Requisitos

- Python 3.14+
- Django 5.2.8
- Virtualenv (recomendado)

## Instalación y ejecución local

1. **Clonar el repositorio**
```bash
git clone <URL_DEL_REPO>
cd <NOMBRE_DEL_REPO>
````

2. **Crear y activar entorno virtual**
```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
````

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
````

4. **Aplicar migraciones**
```bash
python manage.py migrate
````

5. **Crear usuario administrador (opcional)**
```bash
python manage.py createsuperuser
````

6. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
````

7. **Abrir en el navegador**
```bash
http://127.0.0.1:8000/
```

## Funcionalidades

- CRUD de Productos, Categorías y Etiquetas.
- Autenticación de usuarios.
- Navbar compartido con acceso a todas las secciones.
- Interfaz administrativa vía django.contrib.admin.