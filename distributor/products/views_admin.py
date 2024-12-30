from rest_framework import viewsets
from .models import *
from .serializers_admin import *
from .permissions import IsAdminUserRole  # Importa el permiso personalizado para el tipo de usuario que yo quiera
from django.shortcuts import render
from django.views import View

## vistas para redireccionar

class list_categoryView(View):
    def get(self, request):
        return render(request, 'products/admin/categorias/listar_categorias.html')

class list_brandsView(View):
    def get(self, request):
        return render(request, 'products/admin/marcas/listar_marcas.html')

class list_presentacion(View):
    def get(self, request):
        return render(request, 'Products/presentacion/listar_presentacion.html')



class CategoriaViewSetAdmin(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaAdminSerializer

class MarcaViewSetAdmin(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaAdminSerializer

class PresentacionViewSetAdmin(viewsets.ModelViewSet):
    queryset = Presentacion.objects.all()
    serializer_class = PresentacionAdminSerializer

class CartaColorViewSetAdmin(viewsets.ModelViewSet):
    queryset = CartaColor.objects.all()
    serializer_class = CartaColorAdminSerializer
    #permission_classes = [IsAdminUserRole]

class ProductoViewSetAdmin(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoAdminSerializer
    #permission_classes = [IsAdminUserRole]  # Aplica el permiso predeterminado por ahora cuando el usuario se loguee toca tenerlo en cuenta para 
                                            # que no tenga errores en caso de estar testeando 
                                        