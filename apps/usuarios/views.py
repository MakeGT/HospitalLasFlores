from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from apps.usuarios.forms import RegistroForm
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuarios/usuario_nuevo.html"
    form_class = RegistroForm
    success_url = reverse_lazy('listar_producto')

class UsuariosListView(ListView):
    model = User
    template_name = 'usuarios/usuarios_list.html'
    context_object_name ='users'

    def __str__(self):
        return self.email