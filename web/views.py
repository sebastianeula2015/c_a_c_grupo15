from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms_cliente import *
from .forms_producto import *
from .forms_vendedor import *
from .forms_venta import *
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

def venta_consulta(request):

    contexto = {
        'alumnos': [
            'Carlos Lopez',
            'Maria Del Cerro',
            'Gaston Perez'
        ],
        'cuota_al_dia': True
    }
    return render(request, 'web/venta_consulta.html', contexto)


 
##########################################################################################
def cliente_consulta(request):
    contexto = {
        'clientes': [
            'Carlos Lopez',
            'Maria Del Cerro',
            'Gaston Perez'
        ],
        'pago_al_dia': True
    }
    return render(request, 'web/cliente_consulta.html', contexto)

def cliente_listar(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'web/cliente_listar.html', context)
def cliente_nuevo(request):
    contexto = {'form': NuevoClienteForm()}
    if request.method == "GET":
        return render(request, 'web/cliente_nuevo.html', contexto)

    else:  # Asumo que es un POST
        ncliente = NuevoClienteForm(data=request.POST)
        if ncliente.is_valid():
            ncliente.save()
            contexto['mensaje'] = "Cliente guardado"
        else:
            contexto['mensaje'] = ncliente.errors
    return render(request, 'web/cliente_nuevo.html', contexto)


def cliente_modificacion(request, pk):
    try:
        cliente = get_object_or_404(Cliente, pk=pk)

        if request.method == 'POST':
            form = NuevoClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                mensaje_exito = "Cliente editado con éxito."
                context = {'form': form, 'mensaje_exito': mensaje_exito}
                return render(request, 'web/cliente_modificacion.html', context)
        else:
            form = NuevoClienteForm(instance=cliente)

        context = {'form': form}
        return render(request, 'web/cliente_modificacion.html', context)

    except Exception as e:
        mensaje_error = f"Error al editar cliente: {e}"
        context = {'mensaje_error': mensaje_error}
        return render(request, 'web/cliente_modificacion.html', context)


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
 

def venta_nueva(request):
    
    contexto = {}

    if request.method == "GET":
        contexto['alta_alumno_form'] = VentaNuevaForm()
    
    else: # Asumo que es un POST
        contexto['alta_alumno_form'] = VentaNuevaForm(request.POST)
        form = VentaNuevaForm(request.POST)  # form needs content
    
        if form.is_valid():
            print(request.POST)
            return redirect('index')

    return render(request, 'web/venta_nueva.html', contexto)


def venta_modificacion(request):
    
    contexto = {}

    if request.method == "GET":
        contexto['alta_alumno_form'] = VentaModificicacionForm()
    
    else: # Asumo que es un POST
        contexto['alta_alumno_form'] = VentaModificicacionForm(request.POST)
        form = VentaModificicacionForm(request.POST)  # form needs content
    
        if form.is_valid():
            print(request.POST)
            return redirect('index')

    return render(request, 'web/venta_modificacion.html', contexto)

#def alumnos_por_año(request, year):
#    alumnos = ["Carlos", "Maria", "Jose"] # """"Levanta""""" los usuarios de la BBDD
#    return HttpResponse(f"listado de alumnos: {year} \n {alumnos}")
