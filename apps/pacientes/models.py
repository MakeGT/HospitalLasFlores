from django.db import models

# Create your models here.
class Pacientes(models.Model):
    Id = models.AutoField(primary_key=True)
    NombreCompleto = models.CharField(max_length=80, null=False, blank=False)
    Dpi = models.CharField(max_length=15, null=False, blank=False)
    Genero = models.CharField(max_length=1, null=False, blank=False)
    EstadoCivil = models.CharField(max_length=1, null=False, blank=False)
    Direccion = models.CharField(max_length=80, null=False, blank=False)
    FechaNacimiento=models.DateField(auto_now=False)
    Telefono = models.CharField(max_length=8, null=False, blank=False)
    TipoSangre = models.CharField(max_length=1, null=False, blank=False)
    Responsable = models.CharField(max_length=80, null=False, blank=False)
    TelefonoResponsable = models.CharField(max_length=8, null=False, blank=False)
    NombreConyugue = models.CharField(max_length=80, null=False, blank=False)
    Escolaridad = models.CharField(max_length=1, null=False, blank=False) #primaria, básico, diversificado, universidad
    Ocupacion = models.CharField(max_length=80, null=False, blank=False)
    DpiResponsable = models.CharField(max_length=15, null=True, blank=False)
