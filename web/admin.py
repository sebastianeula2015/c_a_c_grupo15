from cProfile import Profile

from django.contrib import admin
from .models import Cliente, provincias, Proveedor, Vendedor, Producto, DetalleVenta

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(DetalleVenta)
