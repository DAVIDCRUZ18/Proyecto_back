from django.shortcuts import render
from .models import Producto,Categoria,Moto
from django.http import JsonResponse
from .serializer import Productoserializers,CategoriaSerializer,MotoSerializer
from rest_framework import generics


# Create your views here.

def Lista_Producto(request):
    productos= Producto.objects.all()
    serializer = Productoserializers(productos,many= True)
    return JsonResponse(serializer.data,safe=False)

def Lista_Categoria(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return JsonResponse(serializer.data, safe=False)


def Lista_Moto(request):
    Motos = Moto.objects.all()
    serializer = MotoSerializer(Motos, many=True)
    return JsonResponse(serializer.data, safe=False)

