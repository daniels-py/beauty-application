from rest_framework import serializers
from .models import *


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'permite_color']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre']


class PresentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentacion
        fields = ['id', 'nombre', 'descripcion']


class CartaColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaColor
        fields = ['id', 'codigo_color', 'nombre_color', 'hexadecimal', 'descripcion', 'marca']

# Serializador para el modelo Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'marca', 'categoria', 'presentacion', 'descripcion', 'carta_color', 'precio']
