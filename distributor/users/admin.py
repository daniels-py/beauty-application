from django.contrib import admin
from .models import CustomUser  # Importamos nuestro modelo personalizado

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Configuración para gestionar usuarios en el panel de administración.
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'role', 'is_active', 'is_online', 'last_login', 'date_joined')  # Columnas visibles
    list_filter = ('role', 'is_active', 'is_online', 'date_joined')  # Filtros para roles, estado, conexión y fecha de registro
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')  # Campos de búsqueda
    readonly_fields = ('last_login', 'date_joined')  # Campos de solo lectura

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Información Adicional', {
            'fields': ('role', 'is_online', 'last_login', 'date_joined')
        }),
    )
