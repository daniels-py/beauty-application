from django.contrib import admin
from .models import Categoria, Marca, Presentacion, CartaColor, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Configuración para gestionar categorías en el panel de administración.
    """
    list_display = ('nombre', 'permite_color')  # Columnas visibles
    search_fields = ('nombre',)  # Campos de búsqueda

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    """
    Configuración para gestionar marcas en el panel de administración.
    """
    list_display = ('nombre',)  # Columnas visibles
    search_fields = ('nombre',)  # Campos de búsqueda

@admin.register(Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    """
    Configuración para gestionar presentaciones en el panel de administración.
    """
    list_display = ('nombre',)  # Columnas visibles
    search_fields = ('nombre',)  # Campos de búsqueda

@admin.register(CartaColor)
class CartaColorAdmin(admin.ModelAdmin):
    """
    Configuración para gestionar cartas de colores en el panel de administración.
    """
    list_display = ('codigo_color', 'nombre_color', 'hexadecimal', 'marca')  # Columnas visibles
    list_filter = ('marca',)  # Filtros para marca
    search_fields = ('codigo_color', 'nombre_color', 'hexadecimal')  # Campos de búsqueda

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """
    Configuración para gestionar productos en el panel de administración.
    """
    list_display = ('nombre', 'marca', 'categoria', 'presentacion', 'carta_color', 'precio', 'codigo_barras')  # Columnas visibles
    list_filter = ('marca', 'categoria', 'presentacion', 'carta_color')  # Filtros para marca, categoría, presentación y carta de color
    search_fields = ('nombre', 'marca__nombre', 'categoria__nombre', 'presentacion__nombre', 'carta_color__nombre_color', 'codigo_barras')  # Campos de búsqueda
    readonly_fields = ('codigo_barras',)  # Campos de solo lectura

    fieldsets = (
        (None, {
            'fields': ('nombre', 'marca', 'categoria', 'presentacion', 'carta_color', 'precio', 'codigo_barras')
        }),
    )
