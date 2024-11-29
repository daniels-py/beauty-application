# inventory/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventarioViewSet

router = DefaultRouter()
router.register(r'inventarios', InventarioViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluye las URLs generadas por el router
]
