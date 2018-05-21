from django.db import models
from apps.inventario.models import Pedidos
from apps.consultas.models import Visitas
# Create your models here.

class Clientes(models.Model):
    Id = models.AutoField(primary_key=True) 
    Nombre = models.CharField(max_length=80, null=False, blank=False)
    Nit = models.CharField(max_length=15, null=False, blank=False)

class Cobros(models.Model):
    Id = models.AutoField(primary_key=True)    
    #UsuarioId
    ClienteId = models.ForeingKey('Clientes', null=False, blank=False)
    MontoTotal = models.FloatField(null=False, blank=False)
    Estado = models.CharField(max_length=1, null=False, blank=False)

class DetalleCobros(models.Model):
    Id = models.AutoField(primary_key=True)   
    PedidoId = models.ForeingKey('Pedidos', null=False, blank=False)
    VisitaId = models.ForeingKey('Visitas', null=False, blank=False)
    CobroId = models.ForeingKey('Cobros', null=False, blank=False)
    Estado = models.CharField(max_length=1, null=False, blank=False)
