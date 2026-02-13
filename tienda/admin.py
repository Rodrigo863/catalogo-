from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    prepopulated_fields = {"slug": ("nombre",)}
    search_fields = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "activo", "categoria", "creado")
    list_filter = ("activo", "categoria")
    search_fields = ("nombre", "descripcion")
    prepopulated_fields = {"slug": ("nombre",)}
