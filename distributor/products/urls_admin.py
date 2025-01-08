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
     path('Panel/', panel, name="Home" ),

]
