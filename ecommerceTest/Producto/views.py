from django.shortcuts import render
from .models import Producto,Categoria
from django.http import JsonResponse
from .serializer import Productoserializers,CategoriaSerializer
#from rest_framework import generics
#from .serializers import CategoriaSerializer

# Create your views here.

def Lista_Producto(request):
    productos= Producto.objects.all()
    serializer = Productoserializers(productos,many= True)
    return JsonResponse(serializer.data,safe=False)

def Lista_Categoria(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return JsonResponse(serializer.data, safe=False)

