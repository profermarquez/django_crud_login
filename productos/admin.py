# productos/admin.py
from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')  # Campos que se muestran en la lista de productos
    search_fields = ('nombre', 'descripcion')  # Habilitar la búsqueda por nombre y descripción
    list_filter = ('precio', 'stock')  # Filtros para facilitar la búsqueda

