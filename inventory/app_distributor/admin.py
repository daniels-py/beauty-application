from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Marca, Presentacion, CartaColor, Producto, Inventario, CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'role_display')  # Agrega 'role_display' para mostrar el ícono personalizado
    search_fields = ('username', 'email')  # Campos que se pueden buscar en el panel
    list_filter = ('role',)  # Permite filtrar por rol

    def role_display(self, obj):
        # Muestra un círculo de color verde para administradores y azul para empleados
        color = 'green' if obj.role == 'admin' else 'blue'
        return format_html(
            '<span style="display: inline-block; width: 12px; height: 12px; border-radius: 50%; background-color: {};"></span>',
            color
        )

    role_display.short_description = 'Role Status'  # Nombre de la columna en el panel

# Registra el modelo CustomUser con la configuración personalizada
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'permite_color')
    search_fields = ('nombre',)
    list_filter = ('permite_color',)

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(CartaColor)
class CartaColorAdmin(admin.ModelAdmin):
    list_display = ('codigo_color', 'nombre_color', 'hexadecimal', 'marca')
    search_fields = ('codigo_color', 'nombre_color')
    list_filter = ('marca',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'categoria', 'presentacion', 'precio', 'carta_color')
    search_fields = ('nombre', 'marca__nombre')
    list_filter = ('marca', 'categoria', 'presentacion')
    autocomplete_fields = ('marca', 'categoria', 'presentacion', 'carta_color')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'unidades')
    search_fields = ('producto__nombre',)
    list_filter = ('producto__categoria', 'producto__marca')
    autocomplete_fields = ('producto',)
