from django.db import models
from apps.pacientes.models import Pacientes

# Create your models here.
class Visitas(models.Model):
    Id = models.AutoField(primary_key=True) 
    Motivo = models.CharField(max_length=15, null=False, blank=False)
    #MedicoId = 
    PacienteId = models.ForeingKey('Pacientes', null=False, blank=False)  
    Fecha = models.DateField(auto_now=True)
    Diagnostico = models.CharField(max_length=1000, null=False, blank=False)
    ProximaVisita = models.DateField(auto_now=False)
    Costo = models.IntegerField()
    EstadoDeCobro = models.CharField(max_length=1, null=False, blank=False)