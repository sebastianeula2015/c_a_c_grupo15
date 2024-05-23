from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente_consulta', views.cliente_consulta, name='cliente_consulta'),
    path('cliente_nuevo', views.cliente_nuevo, name='cliente_nuevo'),
    path('cliente_modificacion/<int:pk>/', views.cliente_modificacion, name='cliente_modificacion'),
    path('cliente_listar', views.cliente_listar, name='cliente_listar'),
    path('producto_consulta', views.producto_consulta, name='producto_consulta'),
    path('producto_nuevo', views.producto_nuevo, name='producto_nuevo'),
    path('producto_modificacion', views.producto_modificacion, name='producto_modificacion'),
    path('vendedor_consulta', views.vendedor_consulta, name='vendedor_consulta'),
    path('vendedor_nuevo', views.vendedor_nuevo, name='vendedor_nuevo'),
    path('vendedor_modificacion', views.vendedor_modificacion, name='vendedor_modificacion'),
    path('venta_consulta', views.venta_consulta, name='venta_consulta'),
    path('venta_nueva', views.venta_nueva, name='venta_nueva'),            
    path('venta_modificacion', views.venta_modificacion, name='venta_modificacion'),    
]