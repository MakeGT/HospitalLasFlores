from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import ProductoCreateView, ProductoListView, ProductoUpdateView, ProductoDeleteView, LoteListView, LoteDeleteView, LoteUpdateView, LoteCreateView

# Estas son la urls de casos
urlpatterns = [
    url(r'^agregarproducto/', login_required(ProductoCreateView.as_view()), name='agregar_producto'),
    url(r'^listarproducto/', login_required(ProductoListView.as_view()), name='listar_producto'),
    url(r'^eliminarproducto/(?P<pk>\d+)/', login_required(ProductoDeleteView.as_view()), name='eliminar_producto'),
    url(r'^editarproducto/(?P<pk>\d+)/', login_required(ProductoUpdateView.as_view()), name='editar_producto'),
    url(r'^agregarlote/', login_required(LoteCreateView.as_view()), name='agregar_lote'),
    url(r'^listarlote/', login_required(LoteListView.as_view()), name='listar_lote'),
    url(r'^eliminarlote/(?P<pk>\d+)/', login_required(LoteDeleteView.as_view()), name='eliminar_lote'),
    url(r'^editarlote/(?P<pk>\d+)/', login_required(LoteUpdateView.as_view()), name='editar_lote'),
    ]