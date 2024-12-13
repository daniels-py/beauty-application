"""
URL configuration for distributor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar 'include'
from django_browser_reload import urls as browser_reload_urls

urlpatterns = [
    path('admin/', admin.site.urls),



    path('api/products/', include('products.urls')),  # Ruta para el módulo de 'productos'
    path('api/users/', include('users.urls')),    # Incluye las URLs de la aplicación 'users'
    path('api/inventory/', include('inventory.urls')),  # Incluye las URLs de la aplicación 'inventory'
    
    # extencion para cargar automatica en vistar genericas
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += browser_reload_urls.urlpatterns