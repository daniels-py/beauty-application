from django.urls import path
from . import views

urpatterns = [
    path('', views.home, name='store_home'),  # Ruta para la página principal
]