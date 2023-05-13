from django.contrib import admin

from compra.models import Producto, Proveedor

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = [
        "id", 
        "nombre", 
        "precio", 
        "stock_actual", 
        "proveedor", 
        "activo",
    ]
    search_fields = [
        "nombre",
    ]

class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    list_display = [
        "id",
        "nombre",
        "apellido",
        "dni",
    ]


# registrar modelos
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)