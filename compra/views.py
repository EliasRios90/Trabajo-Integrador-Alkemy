from django.contrib import messages
from django.shortcuts import render, redirect
from compra.models import*


# Create your views here.
def inicio(request):

    return render(
        request,
        "compra/inicio.html"
    )



def listado_productos(request):
    listado_productos = Producto.objects.all()
    context = {"listado_productos": listado_productos}
    
    return render(
        request,
        "compra/listado_productos.html",
        context
    )



def listado_proveedores(request):
    listado_proveedores = Proveedor.objects.all()
    context = {"listado_proveedores": listado_proveedores}

    return render(
        request,
        "compra/listado_proveedores.html",
        context
    )



def agregar_proveedor(request):
    listado_proveedores = Proveedor.objects.all()
    context = {"listado_proveedores": listado_proveedores,}

    
    if request.POST:
        nombre_proveedor = request.POST['nombre']
        apellido_proveedor = request.POST['apellido']
        dni_proveedor = request.POST['dni']

        Proveedor.objects.create(
            nombre = nombre_proveedor,
            apellido = apellido_proveedor,
            dni = dni_proveedor
        )
        messages.success(request, f"El proveedor {nombre_proveedor} {apellido_proveedor} se creado correctamente.")

    return render(
        request,
        "compra/agregar_proveedor.html",
        context
    )



def agregar_producto(request):
    listado_proveedores = Proveedor.objects.all()
    context = {
        "listado_proveedores": listado_proveedores,
        }

    
    if request.POST: # se activa cuando se hace click en el boton 'Agregar producto'
        nombre_producto = request.POST['nombre'] # nombre es el que esta en el html
        precio_producto = request.POST['precio']
        stock_producto = request.POST['stock_actual']
        id_proveedor = request.POST['proveedor']
        estado = request.POST.get('estado') == 'on' # determina si se ha tildado o no en el checkbox
        
        Producto.objects.create(
            nombre = nombre_producto,
            precio = precio_producto,
            stock_actual = stock_producto,
            proveedor_id = id_proveedor,
            activo = estado
        )
        messages.success(request, f"El producto {nombre_producto} se creado correctamente.")

    return render(
        request,
        "compra/agregar_producto.html",
        context
    )



def modificar_producto(request, id_producto):
    try:
        listado_proveedores = Proveedor.objects.all()
        producto = Producto.objects.get(id=id_producto)

        context = {
            "listado_proveedores": listado_proveedores,
            "producto": producto
        }

        if request.POST:
            nombre_producto = request.POST["nombre"]
            precio_producto = request.POST["precio"]
            stock = request.POST["stock_actual"]
            id_proveedor = request.POST["proveedor"]

            producto.nombre = nombre_producto
            producto.precio = precio_producto
            producto.stock_actual = stock
            producto.proveedor_id = id_proveedor

            producto.save()
            messages.success(request, f"El producto {producto.nombre} se actualizado.")
    except:
        messages.error(request, f"El producto {producto.nombre} no se puede actualizar.")
        return redirect("productos")
    
    return render(
        request,
        "compra/modificar_producto.html",
        context
    )



def desactivar_producto(request, id_producto):
    try:
        producto = Producto.objects.get(id=id_producto)
        producto.activo = False
        producto.save()
    except:
        messages.error(request, "No se ha encontrado el producto ha desactivar.")

    messages.success(request, f"El producto {producto.nombre} se ha desactivado correctamente.")
    return redirect("productos")



def activar_producto(request, id_producto):
    try:
        producto = Producto.objects.get(id=id_producto)
        producto.activo = True
        producto.save()
    except:
        messages.error(request, "No se ha encontrado el producto ha activar.")

    messages.success(request, f"El producto {producto.nombre} se ha activado correctamente.")

    return redirect("productos")