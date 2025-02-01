from django.db import models
from inventory.models import Inventario  # Si es que el modelo Inventario está en otra app
from products.models import Producto  # Asegúrate de importar correctamente el modelo Producto
from django.db import models
from django.core.validators import MinValueValidator

class Venta(models.Model):
    fecha_venta = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Venta')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Total de la Venta')
    # Si necesitas registrar el cliente (opcional)
    cliente = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nombre del Cliente')
    # Si necesitas un campo para notas adicionales
    notas = models.TextField(blank=True, null=True, verbose_name='Notas adicionales')

    def __str__(self):
        return f'Venta #{self.id} - {self.fecha_venta.strftime("%Y-%m-%d %H:%M")}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles', verbose_name='Venta')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ventas', verbose_name='Producto')
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name='Cantidad')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Unitario')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Subtotal')

    def save(self, *args, **kwargs):
        # Calcula el subtotal automáticamente al guardar
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre} - ${self.subtotal}'

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'