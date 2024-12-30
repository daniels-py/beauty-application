from django.db import models
from inventory.models import Inventario  # Si es que el modelo Inventario está en otra app
from products.models import Producto  # Asegúrate de importar correctamente el modelo Producto


class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la Venta")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total de la Venta")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="ventas")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad Vendida")
    # Podrías agregar más campos, como el cliente, el estado de la venta, etc.

    def save(self, *args, **kwargs):
        # Actualizar el inventario al registrar la venta
        try:
            inventario_producto = Inventario.objects.get(producto=self.producto)
            if inventario_producto.unidades >= self.cantidad:
                # Si hay suficientes unidades, se descuentan del inventario
                inventario_producto.unidades -= self.cantidad
                inventario_producto.save()
            else:
                raise ValueError("No hay suficientes unidades en el inventario")
        except Inventario.DoesNotExist:
            raise ValueError("El producto no existe en el inventario")

        super(Venta, self).save(*args, **kwargs)  # Llamada al método save original

    def __str__(self):
        return f"Venta #{self.id} - {self.producto.nombre}"
