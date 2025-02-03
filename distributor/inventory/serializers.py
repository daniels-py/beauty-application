from rest_framework import serializers
from .models import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    producto_marca = serializers.CharField(source='producto.marca.nombre', read_only=True)
    producto_categoria = serializers.CharField(source='producto.categoria.nombre', read_only=True)
    precio_producto = serializers.DecimalField(source='producto.precio', max_digits=10, decimal_places=2, read_only=True)
    nombrecolor = serializers.CharField(source='producto.carta_color.nombre_color', read_only=True)
    codigo_color = serializers.CharField(source='producto.carta_color.codigo_color', read_only=True)

    class Meta:
        model = Inventario
        fields = ['id', 'producto', 'producto_nombre', 'producto_marca', 'producto_categoria', 'unidades', 'fecha_ingreso','precio_producto','nombrecolor','codigo_color']

    def validate(self, data):
        """
        Validación personalizada para evitar duplicados de productos en el inventario.
        """
        producto = data.get('producto')
        if Inventario.objects.filter(producto=producto).exists():
            raise serializers.ValidationError(f"El producto {producto.nombre} ya está en el inventario.")
        return data