from  rest_framework import serializers
from .models import Producto,Categoria,Moto


class Productoserializers(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields='__all__'

        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'