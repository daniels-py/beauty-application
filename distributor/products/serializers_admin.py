from rest_framework import serializers
from .models import *

class CategoriaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'permite_color']

class MarcaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre']

class PresentacionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentacion
        fields = ['id', 'nombre', 'descripcion']

class CartaColorAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaColor
        fields = ['id', 'codigo_color', 'nombre_color', 'hexadecimal', 'descripcion', 'marca']

class ProductoAdminSerializer(serializers.ModelSerializer):
    categoria = CategoriaAdminSerializer()
    marca = MarcaAdminSerializer()
    presentacion = PresentacionAdminSerializer()
    carta_color = CartaColorAdminSerializer(many=True)  # Relación múltiple

    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'marca', 'categoria', 'presentacion',
            'descripcion', 'carta_color', 'precio', 'stock', 'fecha_creacion'
        ]
