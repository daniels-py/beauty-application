from django.db import models
from products.models import Producto  # Asegúrate de importar correctamente el modelo Producto
from django.utils.timezone import now

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="inventarios")
    unidades = models.PositiveIntegerField()
    fecha_ingreso = models.DateField(default=now, verbose_name="Fecha de Ingreso")  # Cambiado

    def __str__(self):
        return f"{self.producto.nombre} - Unidades: {self.unidades}"

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
