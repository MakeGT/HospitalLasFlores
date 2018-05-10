from django.db import models

# Create your models here.
class Producto(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=80, null=False, blank=False)
    Marca = models.CharField(max_length=80, null=False, blank=False)
    Unidad = models.CharField(max_length=1, null=False, blank=False)
    Cantidad = models.IntegerField(null=True)
    #Cantidad hace referencia a cúantos elementos contiene, por ejemplo una caja
    Existencia = models.IntegerField()
    
class Lote(models.Model):
    Id = models.AutoField(primary_key=True)
    PrecioVenta = models.FloatField()
    ProductoId = models.ForeingKey('Producto', null=False, blank=False)

class Compras(models.Model): #Compras a proveedor
    Id = models.AutoField(primary_key=True)
    PrecioVenta = models.FloatField()
    ProductoId = models.ForeingKey('Producto', null=False, blank=False)   
