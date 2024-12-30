from django.urls import path, include

urlpatterns = [
    path('api/admin/', include('products.urls_admin')),  # Prefijo para admin
    path('api/empleado/', include('products.urls_employee')),  # Prefijo para empleado
]
