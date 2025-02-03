from django.db import models
from inventory.models import Inventario  # Si es que el modelo Inventario está en otra app
from products.models import Producto  # Asegúrate de importar correctamente el modelo Producto
from django.db import models
from django.core.validators import MinValueValidator

