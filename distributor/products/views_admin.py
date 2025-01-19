from rest_framework import viewsets
from .models import *
from .serializers_admin import *
from .permissions import IsAdminUserRole  # Importa el permiso personalizado para el tipo de usuario que yo quiera
from django.shortcuts import render
from django.views import View
from .models import Producto

# Clase que maneja la vista del panel de control del administrador
class PanelDeControl(View):
    def get(self, request):
        context = {'active_page': 'panel_de_control', 'page_title': 'Panel de control'}
        return render(request, 'products/admin/dashboard.html', context)


# Clase que maneja la vista de usuarios
class Usuarios(View):
    def get(self, request):
        context = {'active_page': 'usuarios', 'page_title': 'Usuarios'}
        return render(request, 'products/admin/users.html', context)



# Función que renderiza la plantilla base
def plantilla_base(request):
    context = {'plantilla_base'}
    return render(request, 'products/admin/base.html',)

# Otra función para renderizar un panel
def panel(request):
    context = {'titulo': 'Panel', 'active_page': 'panel'}
    return render(request, 'products/admin/panel.html',)


def pruebas(request):
    return render(request, 'products/admin/pruebas.html',)


# ...existing code...

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
