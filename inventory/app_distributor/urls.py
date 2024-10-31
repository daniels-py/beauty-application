# app_distributor/urls.py
from django.urls import path
from .views import *

urlpatterns = [

    # vistas de inicio 
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),

    # cerrar secion 
    path('logout/', Logout_View, name='logout'),

    # vistas dedicadas 
    path('admin_dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('admin_categorias/', admin_categorias_view, name='admin_categorias'),
     path('dashboard/counts/', get_dashboard_counts, name='dashboard_counts'),  # Ruta para el contador


    path('employee_dashboard/', employee_dashboard_view, name='employee_dashboard'),




    # Categorías
    path('categorias/', ListarCategorias.as_view(), name='listar_categorias'),
    path('categorias/crear/', CrearCategoria.as_view(), name='crear_categoria'),

    # Marcas
    path('marcas/', ListarMarcas.as_view(), name='listar_marcas'),  
    path('marcas/crear/', CrearMarca.as_view(), name='crear_marca'),  

    # Presentaciones
    path('presentaciones/', ListarPresentaciones.as_view(), name='listar_presentaciones'),  
    path('presentaciones/crear/', CrearPresentacion.as_view(), name='crear_presentacion'),

        # Carta de color
    path('cartas-color/', ListarCartasColor.as_view(), name='listar_cartas_color'),  
    path('cartas-color/crear/', CrearCartaColor.as_view(), name='crear_carta_color'),

    # Productos
    path('productos/', ListarProductos.as_view(), name='listar_productos'), 
        

    # Inventario
    path('inventario/', ListarInventario.as_view(), name='listar_inventario'),
    path('inventario/crear/', CrearInventario.as_view(), name='crear_inventario'),
]
