from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views_admin import *

router_admin = DefaultRouter()
router_admin.register(r'categorias', CategoriaViewSetAdmin, basename='admin-categorias')
router_admin.register(r'marcas', MarcaViewSetAdmin, basename='admin-marcas')
router_admin.register(r'presentaciones', PresentacionViewSetAdmin, basename='admin-presentaciones')
router_admin.register(r'cartas-colores', CartaColorViewSetAdmin, basename='admin-cartas-colores')
router_admin.register(r'productos', ProductoViewSetAdmin, basename='admin-productos')

urlpatterns = [
    # Rutas del router de DRF
    path('api/', include(router_admin.urls)),

    # Rutas específicas para redirigir a las plantillas HTML
    path('admin/panel-de-control/', PanelDeControl.as_view(), name='panel_de_control'),
    path('admin/usuarios/', Usuarios.as_view(), name='usuarios'),  # Asegúrate de que esta línea esté presente
    path('admin/productos/', Productos.as_view(), name='productos'),
    path('admin/categorias/', Categorias.as_view(), name='categorias'),
    path('admin/inventario/', Inventario.as_view(), name='inventario'),

    # Rutas para vistas basadas en funciones
    path('admin/base/', plantilla_base, name='plantilla_base'),
    path('admin/panel/', panel, name='panel'),
    path('admin/pruebas/', pruebas, name='pruebas'),
]
