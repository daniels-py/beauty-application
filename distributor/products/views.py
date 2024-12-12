from rest_framework import viewsets
from .models import *
from .serializers import  CategoriaSerializer, MarcaSerializer, PresentacionSerializer, CartaColorSerializer, ProductoSerializer

from .permissions import IsAdminUserRole  # Importa el permiso personalizado

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminUserRole]  # Aplica el permiso

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAdminUserRole]

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAdminUserRole]

class PresentacionViewSet(viewsets.ModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionSerializer
    permission_classes = [IsAdminUserRole]

class CartaColorViewSet(viewsets.ModelViewSet):
    queryset = CartaColor.objects.all()
    serializer_class = CartaColorSerializer
    permission_classes = [IsAdminUserRole]