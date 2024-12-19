from rest_framework import viewsets
from .models import *
from .serializers import  CategoriaSerializer, MarcaSerializer, PresentacionSerializer, CartaColorSerializer, ProductoSerializer
from .permissions import IsAdminUserRole  # Importa el permiso personalizado para el tipo de usuario que yo quiera
from django.shortcuts import render
from django.views import View

## vistas para redireccionar

class list_categoryView(View):
    def get(self, request):
        return render(request, 'products/categorias/listar_categorias.html')

class list_brandsView(View):
    def get(self, request):
        return render(request, 'products/marcas/listar_marcas.html')


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class PresentacionViewSet(viewsets.ModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionSerializer
    permission_classes = [IsAdminUserRole]

class CartaColorViewSet(viewsets.ModelViewSet):
    queryset = CartaColor.objects.all()
    serializer_class = CartaColorSerializer
    permission_classes = [IsAdminUserRole]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminUserRole]  # Aplica el permiso predeterminado por ahora cuando el usuario se loguee toca tenerlo en cuenta para 
                                            # que no tenga errores en caso de estar testeando 
                                        