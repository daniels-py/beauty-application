from rest_framework.routers import DefaultRouter
from .views_admin import (
    CategoriaViewSetAdmin,
    MarcaViewSetAdmin,
    PresentacionViewSetAdmin,
    CartaColorViewSetAdmin,
    ProductoViewSetAdmin,
)

router_admin = DefaultRouter()
router_admin.register(r'categorias', CategoriaViewSetAdmin, basename='admin-categorias')
router_admin.register(r'marcas', MarcaViewSetAdmin, basename='admin-marcas')
router_admin.register(r'presentaciones', PresentacionViewSetAdmin, basename='admin-presentaciones')
router_admin.register(r'cartas-colores', CartaColorViewSetAdmin, basename='admin-cartas-colores')
router_admin.register(r'productos', ProductoViewSetAdmin, basename='admin-productos')

urlpatterns = router_admin.urls
