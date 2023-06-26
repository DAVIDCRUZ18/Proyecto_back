from django.contrib import admin
from .models import Producto,Categoria,Carrito,Pedido,ItemCarrito,Usuario,Comentario,Favorito,Direccion,Venta,Cita
# Register your models here.



admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(Pedido)
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Favorito)
admin.site.register(Direccion)
admin.site.register(Venta)
admin.site.register(Cita)