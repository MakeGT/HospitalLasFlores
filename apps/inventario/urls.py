from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import ProductoCreateView, ProductoListView, ProductoUpdateView

# Estas son la urls de casos
urlpatterns = [
    url(r'^agregarproducto', ProductoCreateView.as_view(), name='agregar_producto'),
    url(r'^listarproducto', ProductoListView.as_view(), name='listar_producto'),
    ]