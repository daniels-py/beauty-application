# products/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PresentacionViewSet, ProductoViewSet, CartaColorViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'presentaciones', PresentacionViewSet)
router.register(r'cartacolor', CartaColorViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluye las URLs generadas por el router
]
