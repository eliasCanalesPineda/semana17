from django.shortcuts import render
from . models import Cliente, Area, empleado, Venta
# Create your views here.
def cliente_lista(request):
    clientes=Cliente.objects.all()
    return render(request, 'clientelista.html',{'clientes':clientes})

def area_lista(request):
    areas=Area.objects.all()
    return render(request, 'areaslista.html',{'areas':areas})

def empleado_lista(request):
    empleados=empleado.objects.all()
    return render(request, 'empleadoslista.html',{'empleados':empleados})

def venta_lista(request):
    ventas=Venta.objects.all()
    return render(request, 'ventaslista.html',{'ventas':ventas})
