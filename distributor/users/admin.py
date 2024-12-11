from django.contrib import admin
from .models import CustomUser  # Importamos nuestro modelo personalizado

# Registramos el modelo en el panel de administración
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Configuración para gestionar usuarios en el panel de administración.
    """
    list_display = ('username', 'email', 'role', 'is_active')  # Columnas visibles
    list_filter = ('role', 'is_active')  # Filtros para roles y estado
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Campos de búsqueda
