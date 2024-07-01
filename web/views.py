from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import View

from .forms_cliente import *
from .forms_producto import *
from .forms_vendedor import *
from .forms_venta import *
from .forms_proveedor import *
import datetime
from django.http import JsonResponse
from django.forms import formset_factory
from django.db import transaction
from .models import Venta, DetalleVenta
import logging
from django.http import HttpResponseServerError
logger = logging.getLogger(__name__)

@login_required(login_url='login')
def index(request):
    # Accedo a la BBDD a traves de los modelos
    contexto = {
        'name': '',
        'fecha_hora': datetime.datetime.now()
    }
    return render(request, 'web/index.html', contexto)

@login_required(login_url='login')
@permission_required
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

 
## CLIENTE #######################################################################################
@login_required(login_url='login')
def cliente_listar(request):
    clientes = Cliente.objects.all()
    return render(request, 'web/cliente_listar.html', {'clientes': clientes})


@login_required(login_url='login')
def cliente_detalles(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'web/cliente_consulta.html', {'cliente': cliente})

@login_required(login_url='login')
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


@login_required(login_url='login')
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

@login_required(login_url='login')
def cliente_eliminar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente')
        return redirect('cliente_listar')
    return render(request, 'web/cliente_eliminar.html', {'cliente': cliente})

## PRODUCTO #########################################################################################


@login_required(login_url='login')
def producto_consulta(request):

    productos = Producto.objects.all()
    return render(request, 'web/producto_consulta.html', {'productos': productos})


@login_required(login_url='login')
def producto_nuevo(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente')
            return redirect('producto_consulta')
    else:
        form = ProductoForm()
    return render(request, 'web/producto_nuevo.html', {'form': form})


@login_required(login_url='login')
def producto_modificacion(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('producto_consulta')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'web/producto_nuevo.html', {'form': form})

@login_required(login_url='login')
def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente')
        return redirect('producto_consulta')
    return render(request, 'web/producto_eliminar.html', {'producto': producto})

@login_required(login_url='login')
def get_precio_producto(request):
    producto_id = request.GET.get('producto_id')
    if producto_id:
        try:
            producto = Producto.objects.get(pk=producto_id)
            data = {'precio': producto.precio}
        except Producto.DoesNotExist:
            data = {'error': 'Producto no encontrado'}
    else:
        data = {'error': 'ID de producto no proporcionado'}
    return JsonResponse(data)
## VENDEDOR ###################################################################################


@login_required(login_url='login')
def vendedor_consulta(request):

    vendedores = Vendedor.objects.all()
    return render(request, 'web/vendedor_consulta.html', {'vendedores': vendedores})

@login_required(login_url='login')
def vendedor_nuevo(request):
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente')
            return redirect('vendedor_consulta')
    else:
        form = VendedorForm()
    return render(request, 'web/vendedor_nuevo.html', {'form': form})

@login_required(login_url='login')
def vendedor_modificacion(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    if request.method == "POST":
        form = VendedorForm(request.POST, instance=vendedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendedor actualizado exitosamente')
            return redirect('vendedor_consulta')
    else:
        form = VendedorForm(instance=vendedor)

    return render(request, 'web/vendedor_nuevo.html', {'form': form})

@login_required(login_url='login')
def vendedor_eliminar(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    if request.method == "POST":
        vendedor.delete()
        messages.success(request, 'Vendedor eliminado exitosamente')
        return redirect('vendedor_consulta')
    return render(request, 'web/vendedor_eliminar.html', {'vendedor': vendedor})
 


# #################################################################################################CRUD para Venta
@login_required(login_url='login')
def venta_list(request):
    ventas = Venta.objects.all()
    return render(request, 'web/venta_list.html', {'ventas': ventas})

@login_required(login_url='login')
def venta_detail(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    return render(request, 'web/venta_detail.html', {'venta': venta})

@login_required(login_url='login')
def venta_mensaje(request, venta_id):
    venta = Venta.objects.get(pk=venta_id)
    context = {
        'venta_id': venta_id,
        'venta': venta,
    }
    return render(request, 'web/venta_mensaje.html', context)

########
@login_required(login_url='login')
def venta_create(request):
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        detalle_venta_formset = DetalleVentaFormSet(request.POST)

        flagProductoObligatorio1 = False

        if venta_form.is_valid() and detalle_venta_formset.is_valid():

            if detalle_venta_formset.is_valid():  # Validate the formset
                for form in detalle_venta_formset:
                    if form.cleaned_data.get('producto') is not None and form.cleaned_data.get('precio') is not None and form.cleaned_data.get('cantidad') is not None:
                        venta = venta_form.save()
                        detalle_venta = form.save(commit=False)
                        detalle_venta.venta = venta
                        detalle_venta.precio_total = detalle_venta.cantidad * detalle_venta.precio  # Update precio_total here
                        detalle_venta.save()
                        flagProductoObligatorio1 = True
                        print("grabando")
                    else:
                        if form.cleaned_data.get('producto') is None and flagProductoObligatorio1 == False:
                            error_message = "Error en el formulario de detalle de venta. Por favor, revise los campos."
                            context = {'venta_form': venta_form, 'detalle_venta_formset': detalle_venta_formset, 'error_message': error_message}                            
                            return render(request, 'web/venta_form.html', context)
                        else:
                            return redirect('venta_mensaje', venta_id=venta.pk)
            else:
                error_message = "Error en el formulario de detalle de venta. Por favor, revise los campos."
                context = {'venta_form': venta_form, 'detalle_venta_formset': detalle_venta_formset, 'error_message': error_message}
        else:
            error_message = "Error, Detalle de Venta. Si selecciona un producto, completo el resto de los campos"
            context = {'venta_form': venta_form, 'detalle_venta_formset': detalle_venta_formset, 'error_message': error_message}
            return render(request, 'web/venta_form.html', context)
    else:
        venta_form = VentaForm()
        detalle_venta_formset = DetalleVentaFormSet()

    return render(request, 'web/venta_form.html', {
        'venta_form': venta_form,
        'detalle_venta_formset': detalle_venta_formset,
    })
################

@login_required(login_url='login')
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

@login_required(login_url='login')
def venta_delete(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == "POST":
        venta.delete()
        messages.success(request, 'Venta eliminada exitosamente')
        return redirect('venta_list')
    return render(request, 'web/venta_confirm_delete.html', {'venta': venta})

# CRUD para DetalleVenta
@login_required(login_url='login')
def detalleventa_list(request):
    detalles = DetalleVenta.objects.all()
    return render(request, 'web/detalleventa_list.html', {'detalles': detalles})

@login_required(login_url='login')
def detalleventa_detail(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    return render(request, 'web/detalleventa_detail.html', {'detalle': detalle})

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def detalleventa_delete(request, pk):
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    if request.method == "POST":
        detalle.delete()
        messages.success(request, 'Detalle de venta eliminado exitosamente')
        return redirect('detalleventa_list')
    return render(request, 'web/detalleventa_confirm_delete.html', {'detalle': detalle})

# CRUD para Proveedor
@login_required(login_url='login')
def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'web/proveedor_list.html', {'proveedores': proveedores})

@login_required(login_url='login')
def proveedor_detail(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'web/proveedor_detail.html', {'proveedor': proveedor})

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
@permission_required('web.add_proveedor', raise_exception=True)
def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        proveedor.delete()
        messages.success(request, 'Proveedor eliminado exitosamente')
        return redirect('proveedor_list')
    return render(request, 'web/proveedor_confirm_delete.html', {'proveedor': proveedor})


class RegistroView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'usuarios/registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'usuarios/registro.html', {'form': form})