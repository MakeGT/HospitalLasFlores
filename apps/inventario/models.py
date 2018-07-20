from django.db import models
from django.db.models import Sum
from django.utils import timezone

# Create your models here.
class Productos(models.Model):
    Id = models.AutoField(primary_key=True)
    Codigo = models.CharField(max_length=5, null=False, blank=False)
    Nombre = models.CharField(max_length=80, null=False, blank=False)
    Marca = models.CharField(max_length=80, null=False, blank=False)
    Unidades = (
        ('1', 'Unidad'),
        ('2', 'Caja')
    )
    Unidad = models.CharField(max_length=1, choices=Unidades, default='1')
    Cantidad = models.IntegerField(blank=True, null=True)
    Precio = models.FloatField(null=False)
    
    #Cantidad hace referencia a cúantos elementos contiene, por ejemplo una caja
    
    @property
    def Existencia(self):
        return self.lotes.aggregate(Sum('Cantidad'))['Cantidad__sum']

    def publish(self):
        self.save()
    
    def __str__(self):
        return '{}'.format(self.Nombre)


class Proveedores(models.Model):
    Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=80, null=False, blank=False)
    Direccion = models.CharField(max_length=80, null=False, blank=False)
    Telefono = models.CharField(max_length=8, null=False, blank=False)    
    
class Lotes(models.Model):
    Id = models.AutoField(primary_key=True)
    PrecioVenta = models.FloatField()
    ProductoId = models.ForeignKey('Productos', null=False, blank=False, related_name='lotes')
    Cantidad = models.IntegerField(null=True)
    Existencia = models.IntegerField(null = True)
    FechaIngreso = models.DateField(auto_now=True)
    def publish(self):
        self.save()

    def __str__(self):
        return self.Id

class Pedidos(models.Model): #Pedidos de clientes
    Id = models.AutoField(primary_key=True)
    FechaHora = models.DateTimeField(auto_now=True)
    #Llave foranea del usuario que lo realiza
    Monto = models.FloatField()
    TiposPedidos = (
        ('1', 'Interno'),
        ('2', 'Externo')
    )
    TipoPedido = models.CharField(max_length=1, choices=TiposPedidos, null=False, blank=False, default='2')

class DetallePedidos(models.Model): #Pedidos de clientes
    Id = models.AutoField(primary_key=True)
    Cantidad = models.IntegerField(default=1)
    LoteId = models.ForeignKey('Lotes', null=False, blank=False)  
    PedidoId = models.ForeignKey('Pedidos', null=True, blank=True)  
    PrecioModificado = models.FloatField(null=True)
    Estados = (
        ('1', 'Activo'),
        ('2', 'Inactivo')
    )
    Estado = models.CharField(max_length=1, choices=Estados, default='1')