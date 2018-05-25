from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from apps.usuarios.forms import RegistroForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuarios/usuario_nuevo.html"
    form_class = RegistroForm
    #success_url = reverse_lazy('')
