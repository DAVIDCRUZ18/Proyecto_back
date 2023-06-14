from django.shortcuts import render
from .serializer import Productoserializers
from .models import Producto
from django.http import JsonResponse

# Create your views here.

def Lista_Producto(request):
    productos= Producto.objects.all()
    serializer = Productoserializers(productos,many= True)
    return JsonResponse(serializer.data,safe=False)
