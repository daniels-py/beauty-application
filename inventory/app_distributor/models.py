from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

# Modelo de usuario personalizado
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('employee', 'Empleado'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return self.username

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True, verbose_name='Nombre de la Categoría')
    descripcion = models.TextField(verbose_name='Descripción de la Categoría', blank=True)
    permite_color = models.BooleanField(default=False, verbose_name='¿Permite Carta de Colores?')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Marca(models.Model):
    nombre = models.CharField(max_length=255, unique=True, verbose_name='Nombre de la Marca')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Presentacion(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre de la Presentación')
    descripcion = models.TextField(verbose_name='Descripción de la Presentación', blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Presentación'
        verbose_name_plural = 'Presentaciones'


class CartaColor(models.Model):
    codigo_color = models.CharField(max_length=50, verbose_name='Código de Color')
    nombre_color = models.CharField(max_length=255, verbose_name='Nombre del Color')
    hexadecimal = models.CharField(max_length=7, verbose_name='Código Hexadecimal', blank=True)
    descripcion = models.TextField(verbose_name='Descripción del Color', blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='cartas_colores')

    class Meta:
        verbose_name = 'Carta de Color'
        verbose_name_plural = 'Cartas de Colores'
        unique_together = ('codigo_color', 'marca')

    def __str__(self):
        return f'{self.nombre_color} ({self.codigo_color}) - {self.marca.nombre}'


class Producto(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Producto')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE, related_name='productos')
    descripcion = models.TextField(verbose_name='Descripción del Producto', default="Descripción no disponible")
    carta_color = models.ForeignKey(CartaColor, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos', verbose_name='Carta de Color')
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Precio')  # Valor por defecto aquí

    def __str__(self):
        return f'{self.nombre} - {self.marca.nombre}'

    def clean(self):
        if self.carta_color and not self.categoria.permite_color:
            raise ValidationError('Este producto no debería tener carta de color asociada, ya que la categoría no lo permite.')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        unique_together = ('nombre', 'marca')


class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventario')
    unidades = models.PositiveIntegerField(default=0, verbose_name='Unidades')

    def __str__(self):
        return f'{self.producto.nombre} - {self.unidades} unidades'

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        unique_together = ('producto',)
