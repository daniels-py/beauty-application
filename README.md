
# Distributor Management System

Un sistema de gestión de inventarios basado en Django, diseñado específicamente para distribuidores de productos de belleza. Este proyecto ofrece un backend robusto utilizando Django REST Framework y una estructura modular para la administración del proyecto

## Authors

- [@daniels-py](https://github.com/daniels-py)


## Instalación


#### Sigue estos pasos para configurar el proyecto en tu entorno local:

#### 1. Clona el repositorio:

```bash
  git clone <https://github.com/daniels-py/beauty-application> 

  cd Distributor

```

#### 2. Crea un entorno virtual:

```bash
python -m venv venv

source venv/bin/activate  # En Windows: venv\Scripts\activate


```

#### 3. Instala las dependencias:

```bash
pip install -r requirements.txt

```

#### 4. Aplica las migraciones y corre el servidor:

```bash

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


```

#### 













#Lecciones Aprendidas

¿Qué aprendiste mientras desarrollabas este proyecto? ¿Qué desafíos enfrentaste y cómo los superaste?
Endpoints de la API

Con las vistas auto-generadas por Django REST Framework, puedes acceder a los siguientes endpoints:

    /api/products/: Gestión de productos. Permite la creación, lectura, actualización y eliminación de productos.
    
    /api/categories/: Gestión de categorías. Permite la creación, lectura, actualización y eliminación de categorías de productos.

    /api/presentations/: Gestión de presentaciones. Permite gestionar las diferentes presentaciones de los productos (por ejemplo, tamaños o envases).

    /api/cartacolor/: Gestión de cartas de colores. Permite gestionar los colores asociados con los productos, como tintes de cabello.
