from rest_framework import viewsets
from .models import *
from .serializers_employee import *
from django.shortcuts import render
from django.views import View


class ProductoEmpleadoViewSet(viewsets.ReadOnlyModelViewSet):# solo lo habilita para poder ver
    queryset = Producto.objects.all()
    serializer_class = ProductoEmpleadoSerializer

class MarcaEmpleadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaEmpleadoSerializer

class CategoriaEmpleadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaEmpleadoSerializer

class PresentacionEmpleadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionEmpleadoSerializer

class CartaColorEmpleadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CartaColor.objects.all()
    serializer_class = CartaColorEmpleadoSerializer                         