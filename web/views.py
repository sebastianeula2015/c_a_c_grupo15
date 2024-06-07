from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from .forms_cliente import *
from .forms_producto import *
from .forms_vendedor import *
from .forms_venta import *
from .forms_proveedor import *
import datetime

def index(request):
    # Accedo a la BBDD a traves de los modelos
    contexto = {
        'name': '',
        'fecha_hora': datetime.datetime.now()
    }
    return render(request, 'web/index.html', contexto)

def producto_consulta(request):

    contexto = {
        'alumnos': [
            'Carlos Lopez',
            'Maria Del Cerro',
            'Gaston Perez'
        ],
        'cuota_al_dia': True
    }
    return render(request, 'web/producto_consulta.html', contexto)

def vendedor_consulta(request):

    contexto = {
        'alumnos': [
            'Carlos Lopez',
            'Maria Del Cerro',
            'Gaston Perez'
        ],
        'cuota_al_dia': True
    }
    return render(request, 'web/vendedor_consulta.html', contexto)

 
##########################################################################################
def cliente_listar(request):
    clientes = Cliente.objects.all()
    return render(request, 'web/cliente_listar.html', {'clientes': clientes})

def cliente_detalles(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'web/cliente_consulta.html', {'cliente': cliente})

def cliente_nuevo(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente')
            return redirect('cliente_listar')
    else:
        form = ClienteForm()
    return render(request, 'web/cliente_nuevo.html', {'form': form})

def cliente_modificacion(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado exitosamente')
            return redirect('cliente_listar')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'web/cliente_nuevo.html', {'form': form})

def cliente_eliminar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente')
        return redirect('cliente_listar')
    return render(request, 'web/cliente_eliminar.html', {'cliente': cliente})

###########################################################################################
def producto_nuevo(request):
    
    contexto = {}

    if request.method == "GET":
        contexto['alta_alumno_form'] = ProductoNuevoForm()
    
    else: # Asumo que es un POST
        contexto['alta_alumno_form'] = ProductoNuevoForm(request.POST)
        form = ProductoNuevoForm(request.POST)  # form needs content
    
        if form.is_valid():
            print(request.POST)
            return redirect('index')

    return render(request, 'web/producto_nuevo.html', contexto)


def producto_modificacion(request):
    
    contexto = {}

    if request.method == "GET":
        contexto['alta_alumno_form'] = ProductoModificacionForm()
    
    else: # Asumo que es un POST
        contexto['alta_alumno_form'] = ProductoModificacionForm(request.POST)
        form = ProductoModificacionForm(request.POST)  # form needs content
    
        if form.is_valid():
            print(request.POST)
            return redirect('index')

    return render(request, 'web/producto_modificacion.html', contexto)


def vendedor_nuevo(request):
    
    contexto = {}

    if request.method == "GET":
        contexto['alta_alumno_form'] = VendedorNuevoForm()
    
    else: # Asumo que es un POST
        contexto['alta_alumno_form'] = VendedorNuevoForm(request.POST)
        form = VendedorNuevoForm(request.POST)  # form needs content
    
        if form.is_valid():
            print(request.POST)
            return redirect('index')

    return render(request, 'web/vendedor_nuevo.html', contexto)


def vendedor_modificacion(request):
    
    contexto = {}

    if request.method == "GET":
        contexto['alta_alumno_form'] = VendedorModificacionForm()
    
    else: # Asumo que es un POST
        contexto['alta_alumno_form'] = VendedorModificacionForm(request.POST)
        form = VendedorModificacionForm(request.POST)  # form needs content
    
        if form.is_valid():
            print(request.POST)
            return redirect('index')

    return render(request, 'web/vendedor_modificacion.html', contexto)
 


# #################################################################################################CRUD para Venta
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'web/venta_list.html', {'ventas': ventas})

def venta_detail(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    return render(request, 'web/venta_detail.html', {'venta': venta})

def venta_create(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta creada exitosamente')
            return redirect('venta_list')
    else:
        form = VentaForm()
    return render(request, 'web/venta_form.html', {'form': form})

def venta_update(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta actualizada exitosamente')
            return redirect('venta_list')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'web/venta_form.html', {'form': form})

def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        venta.delete()
        messages.success(request, 'Venta eliminada exitosamente')
        return redirect('venta_list')
    return render(request, 'web/venta_confirm_delete.html', {'venta': venta})

# CRUD para DetalleVenta
def detalleventa_list(request):
    detalles = DetalleVenta.objects.all()
    return render(request, 'web/detalleventa_list.html', {'detalles': detalles})

def detalleventa_detail(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    return render(request, 'web/detalleventa_detail.html', {'detalle': detalle})

def detalleventa_create(request):
    if request.method == "POST":
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Detalle de venta creado exitosamente')
            return redirect('detalleventa_list')
    else:
        form = DetalleVentaForm()
    return render(request, 'web/detalleventa_form.html', {'form': form})

def detalleventa_update(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    if request.method == "POST":
        form = DetalleVentaForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Detalle de venta actualizado exitosamente')
            return redirect('detalleventa_list')
    else:
        form = DetalleVentaForm(instance=detalle)
    return render(request, 'web/detalleventa_form.html', {'form': form})

def detalleventa_delete(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    if request.method == "POST":
        detalle.delete()
        messages.success(request, 'Detalle de venta eliminado exitosamente')
        return redirect('detalleventa_list')
    return render(request, 'web/detalleventa_confirm_delete.html', {'detalle': detalle})

# CRUD para Proveedor
def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'web/proveedor_list.html', {'proveedores': proveedores})

def proveedor_detail(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'web/proveedor_detail.html', {'proveedor': proveedor})

def proveedor_create(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor creado exitosamente')
            return redirect('proveedor_list')
    else:
        form = ProveedorForm()
    return render(request, 'web/proveedor_form.html', {'form': form})

def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado exitosamente')
            return redirect('proveedor_list')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'web/proveedor_form.html', {'form': form})

def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        proveedor.delete()
        messages.success(request, 'Proveedor eliminado exitosamente')
        return redirect('proveedor_list')
    return render(request, 'web/proveedor_confirm_delete.html', {'proveedor': proveedor})
