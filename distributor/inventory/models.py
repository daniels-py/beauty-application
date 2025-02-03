# inventory/models.py
from django.db import models
from products.models import Producto  # Asegúrate de importar el modelo Producto
from django.core.exceptions import ValidationError

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventario_inventory')
    unidades = models.PositiveIntegerField(default=0, verbose_name='Unidades Disponibles')
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name='Fecha de Ingreso')

    def __str__(self):
        return f'{self.producto.nombre} - {self.unidades} unidades'

    def clean(self):
        # Validación para evitar duplicación de productos en el inventario
        if Inventario.objects.filter(producto=self.producto).exists():
            raise ValidationError(f"El producto {self.producto.nombre} ya está en el inventario.")

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
