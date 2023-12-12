from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto_Proteccion, Producto_almacen
from .forms import FormsProducto_Proteccion, FormsProducto_almacen
from collections import Counter


def buscar_producto_proteccion(request):
    query = request.GET.get('q', '')
    Proteccion = Producto_Proteccion.objects.filter(nombre_icontains=query)
    return render(request, '', {
        'Proteccion':Proteccion,
    })

def buscar_producto_almacen(request):
    query = request.GET.get('q', '')
    Almacen = Producto_almacen.objects.filter(nombre_icontains=query)
    return render(request, '', {
        'Almacen':Almacen,
    })

