from rest_framework import serializers
from .models import *

class CategoriaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'permite_color']

class MarcaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre']

class PresentacionAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentacion
        fields = ['id', 'nombre']

class CartaColorAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaColor
        fields = ['id', 'codigo_color', 'nombre_color', 'hexadecimal', 'marca']

class ProductoAdminSerializer(serializers.ModelSerializer):
    categoria = CategoriaAdminSerializer()
    marca = MarcaAdminSerializer()
    presentacion = PresentacionAdminSerializer()
    carta_color = CartaColorAdminSerializer()  # Relación múltiple

    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'marca', 'categoria', 'presentacion',
            'carta_color', 'precio'
        ]
