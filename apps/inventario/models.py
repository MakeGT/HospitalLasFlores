from django.db import models

# Create your models here.
class Productos(models.Model):
    Id = models.AutoField(primary_key=True)
    Codigo = models.CharField(max_length=5, null=False, blank=False)
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
    ProductoId = models.ForeignKey('Productos', null=False, blank=False)

class Compras(models.Model): #Compras a proveedor
    Id = models.AutoField(primary_key=True)
    PrecioVenta = models.FloatField()
    ProductoId = models.ForeignKey('Productos', null=False, blank=False)   

class DetalleCompras(models.Model):
    Id = models.AutoField(primary_key=True)
    PrecioVenta = models.FloatField()
    LoteId = models.ForeignKey('Lotes', null=False, blank=False)   
    CompraId = models.ForeignKey('Compras', null=False, blank=False)

class Pedidos(models.Model): #Pedidos de clientes
    Id = models.AutoField(primary_key=True)
    FechaHora = models.DateTimeField(auto_now=True)
    #Llave foranea del usuario que lo realiza
    Monto = models.FloatField()
    TipoPedido = models.CharField(max_length=1, null=False, blank=False)

class DetallePedidos(models.Model): #Pedidos de clientes
    Id = models.AutoField(primary_key=True)
    Cantidad = models.IntegerField
    LoteId = models.ForeignKey('Lotes', null=False, blank=False)  
    PedidoId = models.ForeignKey('Pedidos', null=False, blank=False)  
    PrecioModificado = models.FloatField()
    Estado = models.CharField(max_length=1, null=False, blank=False)