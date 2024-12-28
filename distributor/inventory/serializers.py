from rest_framework import serializers
from .models import Inventario

class InventarioSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre')
    producto_marca = serializers.CharField(source='producto.marca.nombre')
    producto_categoria = serializers.CharField(source='producto.categoria.nombre')

    class Meta:
        model = Inventario
        fields = ['id', 'producto', 'producto_nombre', 'producto_marca', 'producto_categoria', 'unidades']
