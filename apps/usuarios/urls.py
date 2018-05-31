from django.conf.urls import url
from apps.usuarios.views import RegistroUsuario, UsuariosListView
urlpatterns =[
    url(r'^registrar', RegistroUsuario.as_view(), name = "registrar_usuarios"),
    url(r'^listar', UsuariosListView.as_view(), name = "listar_usuarios")
]