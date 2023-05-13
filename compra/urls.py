from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path("productos/", views.listado_productos, name="productos"),
    path("proveedores/", views.listado_proveedores, name="proveedores"),
    path("producto/agrega_producto/", views.agregar_producto, name="agrega_producto"),
    path("proveedor/agrega_proveedor/", views.agregar_proveedor, name="agrega_proveedor"),
    path("productos/modificar/<int:id_producto>", views.modificar_producto, name="modificar_producto"),
    path("productos/desactivar/<int:id_producto>", views.desactivar_producto, name="desactivar_producto"),
    path("productos/activar/<int:id_producto>", views.activar_producto, name="activar_producto"),
]