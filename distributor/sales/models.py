from django.db import models
from inventory.models import Inventario  # Si es que el modelo Inventario está en otra app
from products.models import Producto  # Asegúrate de importar correctamente el modelo Producto


class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la Venta")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total de la Venta", default=0.00)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="ventas")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad Vendida")

    def save(self, *args, **kwargs):
        # Calcular el total de la venta basado en el precio y la cantidad
        self.total = self.producto.precio * self.cantidad

        # También puedes actualizar el inventario aquí, como lo hiciste antes
        try:
            inventario_producto = Inventario.objects.get(producto=self.producto)
            if inventario_producto.unidades >= self.cantidad:
                inventario_producto.unidades -= self.cantidad
                inventario_producto.save()
            else:
                raise ValueError("No hay suficientes unidades en el inventario")
        except Inventario.DoesNotExist:
            raise ValueError("El producto no existe en el inventario")

        super(Venta, self).save(*args, **kwargs)  # Llamada al método save original

    def __str__(self):
        return f"Venta #{self.id} - {self.producto.nombre}"