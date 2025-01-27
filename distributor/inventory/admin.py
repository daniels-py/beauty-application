from django.contrib import admin
from .models import Inventario

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    """
    Configuración para gestionar inventarios en el panel de administración.
    """
    list_display = ('producto', 'unidades', 'fecha_ingreso')  # Columnas visibles
    list_filter = ('fecha_ingreso',)  # Filtros para fecha de ingreso
    search_fields = ('producto__nombre',)  # Campos de búsqueda

    fieldsets = (
        (None, {
            'fields': ('producto', 'unidades', 'fecha_ingreso')
        }),
    )

# Register your models here.
