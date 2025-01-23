# inventory/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_admin import InventarioViewSet

router_admin = DefaultRouter()
router_admin.register(r'inventarios', InventarioViewSet)

urlpatterns = [
    # Rutas del router de DRF
    path('api/', include(router_admin.urls)),  # Incluye las URLs generadas por el router
]
