from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models import Productos
from .models import Proveedores
from .models import Lotes
from .models import Compras
from .models import DetalleCompras
from .models import Pedidos
from .models import DetallePedidos
# Create your views here.

class ProductoCreateView(CreateView):
    model = Productos
    fields = [
        'Codigo',
        'Nombre',
        'Marca',
        'Unidad',
        'Cantidad',
    ]
    template_name = 'inventario/productos_create.html'
    success_url = reverse_lazy('listar_producto')

class ProductoListView(ListView):
    model = Productos
    template_name = 'inventario/productos_list.html'
    context_object_name ='Productos'

    def __str__(self):
        return self.Nombre

class ProductoUpdateView(UpdateView):
    model = Productos
    fields = [
        'Codigo',
        'Nombre',
        'Marca',
        'Unidad',
        'Cantidad'
    ]

    template_name = 'inventario/productos_create.html'
    success_url = reverse_lazy('listar_producto')

class ProductoDeleteView(DeleteView):
    model = Productos

    template_name = 'inventario/productos_delete.html'
    success_url = reverse_lazy('listar_producto')

class ProductoDetailView(DetailView):
    model = Productos
    template_name = 'inventario/producto_detail.html'
    success_url = reverse_lazy('listar_producto')


class LoteCreateView(CreateView):
    model = Lotes
    fields = [
        'PrecioVenta',
        'ProductoId',
        'Cantidad'
    ]
    template_name = 'inventario/lote_create.html'
    success_url = reverse_lazy('listar_lote')

    def get_context_data(self, **kwargs):
        ctx = super(LoteCreateView, self).get_context_data(**kwargs)

        ctx['producto'] = Productos.objects.get(
                pk=self.request.GET.get('producto_id')
            )
        return ctx

class LoteListView(ListView):
    model = Lotes
    template_name = 'inventario/lote_list.html'
    context_object_name ='Lotes'

    def __str__(self):
        return self.Nombre

class LoteDeleteView(DeleteView):
    model = Lotes

    template_name = 'inventario/lote_delete.html'
    success_url = reverse_lazy('listar_lote')

class LoteUpdateView(UpdateView):
    model = Lotes
    fields = [
        'PrecioVenta',
        'ProductoId',
        'Cantidad'
    ]
    template_name = 'inventario/lote_create.html'
    success_url = reverse_lazy('listar_lote')