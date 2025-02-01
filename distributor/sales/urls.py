from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VentaViewSet, DetalleVentaViewSet   # Importa la vista DetalleVentaViewSet

router = DefaultRouter()
router.register(r'ventas', VentaViewSet)
router.register(r'detalleventas', DetalleVentaViewSet)  # Registra la vista DetalleVentaViewSet

urlpatterns = [
    path('', include(router.urls)),  # Incluye todas las rutas registradas en el router
]
