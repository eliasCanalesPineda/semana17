"""
URL configuration for Tarea17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from prueba1.views import cliente_lista,area_lista,empleado_lista,venta_lista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("prueba1.urls")),
    path('',cliente_lista,name='clientelista'),
    path('',area_lista,name='arealista'),
    path('',empleado_lista,name='empleadolista'),
    path('',venta_lista,name='ventalista'),
]
