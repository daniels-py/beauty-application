from rest_framework import viewsets
from .models import *
from .serializers import  CategoriaSerializer, MarcaSerializer, PresentacionSerializer, CartaColorSerializer, ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class PresentacionViewSet(viewsets.ModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionSerializer

class CartaColorViewSet(viewsets.ModelViewSet):
    queryset = CartaColor.objects.all()
    serializer_class = CartaColorSerializer
