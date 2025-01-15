from rest_framework import serializers
from .models import *

class CategoriaEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']  # Ocultamos detalles como 'descripcion' y 'permite_color'

class MarcaEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombre']

class PresentacionEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentacion
        fields = ['id', 'nombre']  # Ocultamos 'descripcion'

class CartaColorEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartaColor
        fields = ['id', 'cdigo_coloro', 'nombre_color', 'hexadecimal']  # Eliminamos 'descripcion' y 'marca'

class ProductoEmpleadoSerializer(serializers.ModelSerializer):
    categoria = CategoriaEmpleadoSerializer()
    marca = MarcaEmpleadoSerializer()
    presentacion = PresentacionEmpleadoSerializer()
    carta_color = CartaColorEmpleadoSerializer() 

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'marca', 'categoria', 'presentacion', 'precio' , 'carta_color','codigo_color']
