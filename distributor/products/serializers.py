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
    # Esto es para poder asociar la marca con el ID en lugar del nombre
    marca = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all())

    class Meta:
        model = CartaColor
        fields = ['id', 'codigo_color', 'nombre_color', 'hexadecimal', 'marca']



class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    marca_nombre = serializers.CharField(source='marca.nombre', read_only=True)
    presentacion_nombre = serializers.CharField(source='presentacion.nombre', read_only=True)
    carta_color_nombre = serializers.CharField(source='carta_color.nombre_color', read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'marca', 'marca_nombre', 'categoria', 'categoria_nombre',
            'presentacion', 'presentacion_nombre', 'carta_color', 'carta_color_nombre',
            'precio', 'codigo_barras'
        ]
    
    def validate(self, data):
        """
        Validaciones personalizadas:
        1. Si la categoría no permite colores, carta_color debe ser nula.
        2. La carta de color debe pertenecer a la misma marca que el producto.
        """
        categoria = data.get('categoria')
        carta_color = data.get('carta_color')
        marca = data.get('marca')

        if categoria and not categoria.permite_color and carta_color:
            raise serializers.ValidationError("La categoría seleccionada no permite carta de color.")

        if carta_color and marca and carta_color.marca != marca:
            raise serializers.ValidationError("La carta de color no pertenece a la misma marca que el producto.")

        return data
