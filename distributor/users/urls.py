from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UsuarioViewSet, RegisterUserView, RegistroUsuarioView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    # Rutas del router de DRF
    path('', include(router.urls)),

    # Ruta para la vista de registro de usuario
    path('api/registro/', RegistroUsuarioView.as_view(), name='api_registro'),

    # Rutas específicas para redirigir a las plantillas HTML
    path('registro/', RegisterUserView.as_view(), name='registro'),
]