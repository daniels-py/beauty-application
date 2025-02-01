from django.db import models
from django.forms import ValidationError


class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True, verbose_name='Nombre de la Categoría')
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

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Presentación'
        verbose_name_plural = 'Presentaciones'


class CartaColor(models.Model):
    codigo_color = models.CharField(max_length=50, verbose_name='Código de Color')
    nombre_color = models.CharField(max_length=255, verbose_name='Nombre del Color')
    hexadecimal = models.CharField(max_length=7, verbose_name='Código Hexadecimal', blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='cartas_colores')

    class Meta:
        verbose_name = 'Carta de Color'
        verbose_name_plural = 'Cartas de Colores'
        unique_together = ('codigo_color', 'marca')  # Evita códigos de color duplicados por marca

    def __str__(self):
        return f'{self.nombre_color} ({self.codigo_color}) - {self.marca.nombre}'


class Producto(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Producto')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE, related_name='productos')
    carta_color = models.ForeignKey(
        CartaColor, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='productos', 
        verbose_name='Carta de Color'
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Precio')
    codigo_barras = models.CharField(max_length=100, unique=True, null=True, blank=True, default="SIN_CODIGO", verbose_name="Código de Barras")

    def __str__(self):
        return f'{self.nombre} - {self.marca.nombre}'

    def clean(self):
        # Validación 1: Si la categoría no permite color, no se debe asignar una carta de color
        if self.carta_color and not self.categoria.permite_color:
            raise ValidationError('Este producto no debería tener carta de color asociada, ya que la categoría no lo permite.')
        
        # Validación 2: La carta de color debe pertenecer a la misma marca que el producto
        if self.carta_color and self.carta_color.marca != self.marca:
            raise ValidationError('La carta de color asociada no pertenece a la misma marca que el producto.')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        unique_together = ('nombre', 'marca')  # Evita productos duplicados por marca