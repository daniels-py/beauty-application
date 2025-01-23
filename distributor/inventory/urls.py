from django.urls import path, include


urlpatterns = [
    path('admin/api/', include('inventory.urls_admin')),  # Prefijo para admin
    
]
