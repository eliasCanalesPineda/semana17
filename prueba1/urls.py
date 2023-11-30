from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.cliente_lista,name='clientelista'),
    path('areas/', views.area_lista,name='arealista'),
    path('empleados/', views.empleado_lista,name='empleadolista'),
    path('ventas/', views.venta_lista,name='ventalista'),
]