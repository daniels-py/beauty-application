from rest_framework.routers import DefaultRouter
from .views_employee import (
    CategoriaEmpleadoViewSet,
    MarcaEmpleadoViewSet,
    PresentacionEmpleadoViewSet,
    CartaColorEmpleadoViewSet,
    ProductoEmpleadoViewSet,
)

router_employee = DefaultRouter()
router_employee.register(r'categorias', CategoriaEmpleadoViewSet, basename='employee-categorias')
router_employee.register(r'marcas', MarcaEmpleadoViewSet, basename='employee-marcas')
router_employee.register(r'presentaciones', PresentacionEmpleadoViewSet, basename='employee-presentaciones')
router_employee.register(r'cartas-colores', CartaColorEmpleadoViewSet, basename='employee-cartas-colores')
router_employee.register(r'productos', ProductoEmpleadoViewSet, basename='employee-productos')

urlpatterns = router_employee.urls
