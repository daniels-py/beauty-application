from django.urls import path, include

urlpatterns = [
    path('admin/', include('products.urls_admin')),  # Rutas para administradores
    path('empleado/', include('products.urls_empleado')),  # Rutas para empleados
]
