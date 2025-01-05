from rest_framework import serializers
from .models import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    producto_marca = serializers.CharField(source='producto.marca.nombre', read_only=True)
    producto_categoria = serializers.CharField(source='producto.categoria.nombre', read_only=True)
    precio_producto = serializers.DecimalField(source='producto.precio', max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = Inventario
        fields = ['id', 'producto', 'producto_nombre', 'producto_marca', 'producto_categoria', 'unidades', 'fecha_ingreso','precio_producto']
