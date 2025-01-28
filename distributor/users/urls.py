from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    # Rutas del router de DRF
    path('', include(router.urls)),

    # Rutas específicas para redirigir a las plantillas HTML

    # Rutas para vistas basadas en funciones

]