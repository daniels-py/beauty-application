# products/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'marcas',  MarcaViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'presentaciones', PresentacionViewSet)
router.register(r'cartacolor', CartaColorViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluye las URLs generadas por el router
    path('listar-categorias/', list_categoryView.as_view(), name='categorias-lista'),
    path('listar-marcas/',list_brandsView.as_view(), name='marcas-lista' ),
    path('listar-presentaciones/', list_presentacion.as_view(), name='presentaciones-listar')
]
