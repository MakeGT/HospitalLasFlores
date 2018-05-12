from django.db import models

# Create your models here.
class Productos(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=80, null=False, blank=False)
    Marca = models.CharField(max_length=80, null=False, blank=False)
    Unidad = models.CharField(max_length=1, null=False, blank=False)
    Cantidad = models.IntegerField(null=True)
    #Cantidad hace referencia a cúantos elementos contiene, por ejemplo una caja
    Existencia = models.IntegerField()

    class Proveedores(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=80, null=False, blank=False)
    Direccion = models.CharField(max_length=80, null=False, blank=False)
    Telefono = models.CharField(max_length=8, null=False, blank=False)    
    
class Lotes(models.Model):
    Id = models.AutoField(primary_key=True)
    PrecioVenta = models.FloatField()
    ProductoId = models.ForeingKey('Producto', null=False, blank=False)

class Compras(models.Model): #Compras a proveedor
    Id = models.AutoField(primary_key=True)
    PrecioVenta = models.FloatField()
    ProductoId = models.ForeingKey('Producto', null=False, blank=False)   

class DetalleCompras(models.Model):
    Id = models.AutoField(primary_key=True)
    PrecioVenta = models.FloatField()
    LoteId = models.ForeingKey('Lotes', null=False, blank=False)   
    CompraId = models.ForeingKey('Compras', null=False, blank=False)

class Pedidos(models.Model): #Pedidos de clientes
    Id = models.AutoField(primary_key=True)
    FechaHora = models.DateTimeField(auto_now=True)
    Estado = models.CharField(max_length=1, null=False, blank=False)
    #Llave foranea del usuario que lo realiza
    Monto = models.FloatField()

class DetallePedidos(models.Model): #Pedidos de clientes
    Id = models.AutoField(primary_key=True)
    Cantidad = models.IntegerField
    LoteId = models.ForeingKey('Lotes', null=False, blank=False)  
    PedidoId = models.ForeingKey('Pedidos', null=False, blank=False)  