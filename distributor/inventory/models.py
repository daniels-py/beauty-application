from django.db import models
from products.models import Producto

# Create your models here.

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventario')
    unidades = models.PositiveIntegerField(default=0, verbose_name='Unidades')

    def __str__(self):
        return f'{self.producto.nombre} - {self.unidades} unidades'

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        unique_together = ('producto',)