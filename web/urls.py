from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente_nuevo', views.cliente_nuevo, name='cliente_nuevo'),
    path('cliente_modificacion/<int:pk>/', views.cliente_modificacion, name='cliente_modificacion'),
    path('cliente_eliminar/<int:pk>/', views.cliente_eliminar, name='cliente_eliminar'),
    path('cliente_detalles/<int:pk>/', views.cliente_detalles, name='cliente_detalles'),
    path('cliente_listar', views.cliente_listar, name='cliente_listar'),

    path('producto_nuevo', views.producto_nuevo, name='producto_nuevo'),
    path('producto_modificacion/<int:pk>/', views.producto_modificacion, name='producto_modificacion'),
    path('producto_eliminar/<int:pk>/', views.producto_eliminar, name='producto_eliminar'),
    path('producto_consulta', views.producto_consulta, name='producto_consulta'),
    path('get_precio_producto/', views.get_precio_producto, name='get_precio_producto'),

    path('vendedor_nuevo', views.vendedor_nuevo, name='vendedor_nuevo'),
    path('vendedor_modificacion/<int:pk>/', views.vendedor_modificacion, name='vendedor_modificacion'),
    path('vendedor_eliminar/<int:pk>/', views.vendedor_eliminar, name='vendedor_eliminar'),
    path('vendedor_consulta', views.vendedor_consulta, name='vendedor_consulta'),

    path('ventas/', views.venta_list, name='venta_list'),
    path('ventas/<int:pk>/', views.venta_detail, name='venta_detail'),
    path('ventas_nueva', views.venta_create, name='venta_create'),
    path('ventas/<int:pk>/editar/', views.venta_update, name='venta_update'),
    path('ventas/<int:pk>/eliminar/', views.venta_delete, name='venta_delete'),
    path('ventas/venta_mensaje/<int:venta_id>/', views.venta_mensaje, name='venta_mensaje'),


    path('detalleventas/', views.detalleventa_list, name='detalleventa_list'),
    path('detalleventas/<int:pk>/', views.detalleventa_detail, name='detalleventa_detail'),
    path('detalleventas/nueva/', views.detalleventa_create, name='detalleventa_create'),
    path('detalleventas/<int:pk>/editar/', views.detalleventa_update, name='detalleventa_update'),
    path('detalleventas/<int:pk>/eliminar/', views.detalleventa_delete, name='detalleventa_delete'),

    path('proveedor_list/', views.proveedor_list, name='proveedor_list'),
    path('proveedores/<int:pk>/', views.proveedor_detail, name='proveedor_detail'),
    path('proveedores/nuevo/', views.proveedor_create, name='proveedor_create'),
    path('proveedores/<int:pk>/editar/', views.proveedor_update, name='proveedor_update'),
    path('proveedores/<int:pk>/eliminar/', views.proveedor_delete, name='proveedor_delete'),

    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('cambiar_contrasena/',
         auth_views.PasswordChangeView.as_view(template_name='usuarios/cambiar_contrasena.html', success_url='/'),
         name='cambiar_contrasena'),
    path('resetear_contrasena/',
         auth_views.PasswordResetView.as_view(template_name='usuarios/resetear_contrasena.html'),
         name='resetear_contrasena'),
    path('resetear_contrasena/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='usuarios/resetear_contrasena_done.html'),
         name='password_reset_done'),
    path('resetear_contrasena/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='usuarios/resetear_contrasena_confirm.html'),
         name='password_reset_confirm'),
    path('resetear_contrasena/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='usuarios/resetear_contrasena_complete.html'),
         name='password_reset_complete'),

]