from rest_framework import serializers
from .models import Categoria, Marca, Presentacion, CartaColor, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'permite_color']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre']

class PresentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentacion
        fields = ['id', 'nombre']

class CartaColorSerializer(serializers.ModelSerializer):
    # esto es para poder ver la marca en el serializer asociado a mi carta de color 
    marca = serializers.StringRelatedField()

    class Meta:
        model = CartaColor
        fields = ['id', 'codigo_color', 'nombre_color', 'hexadecimal', 'marca']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'marca', 'categoria', 'presentacion', 'carta_color', 'precio', 'codigo_barras']
