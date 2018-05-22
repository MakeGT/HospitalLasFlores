from django.conf.urls import url
from django.contrib import admin
from .views import PacienteCreateView, PacienteListView, PacienteUpdateView, PacienteDeleteView

urlpatterns = [
    #url(r'^nuevo/', PacienteCreateView , name='nuevo_paciente'),
    #url(r'^eliminar/(?P<pk>\d+)/', PacienteDeleteView , name='elimninar_paciente'),
    #url(r'^listar/', PacienteListView , name='listar_paciente'),
    #url(r'^editar/(?P<pk>\d+)/', PacienteUpdateView , name='editar_paciente'),
]