from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
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

from .models import Pedidos
from .models import DetallePedidos
from contextlib import contextmanager
# Create your views here.

class ProductoCreateView(CreateView):
    model = Productos
    fields = [
        'Codigo',
        'Nombre',
        'Marca',
        'Unidad',
        'Cantidad',
        'Precio',
    ]
    template_name = 'inventario/productos_create.html'
    success_url = reverse_lazy('listar_producto')

    @method_decorator(permission_required('productos.añadir_producto',reverse_lazy('listar_producto')))
    def dispatch(self, *args, **kwargs):
        return super(ProductoCreateView, self).dispatch(*args, **kwargs)

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
        'Cantidad',
        'Precio',
    ]

    template_name = 'inventario/productos_create.html'
    success_url = reverse_lazy('listar_producto')

    @method_decorator(permission_required('productos.editar_producto',reverse_lazy('listar_producto')))
    def dispatch(self, *args, **kwargs):
        return super(ProductoUpdateView, self).dispatch(*args, **kwargs)
    

class ProductoDeleteView(DeleteView):
    model = Productos

    template_name = 'inventario/productos_delete.html'
    success_url = reverse_lazy('listar_producto')

    @method_decorator(permission_required('productos.eliminar_producto',reverse_lazy('listar_producto')))
    def dispatch(self, *args, **kwargs):
        return super(ProductoDeleteView, self).dispatch(*args, **kwargs)

class ProductoDetailView(DetailView):
    model = Productos
    template_name = 'inventario/producto_detail.html'
    success_url = reverse_lazy('listar_producto')


class LoteCreateView(CreateView):
    model = Lotes
    fields = [
        'PrecioVenta',
        'ProductoId',
        'Cantidad',
        'Existencia'
    ]
    template_name = 'inventario/lote_create.html'
    success_url = reverse_lazy('listar_producto')

    def get_context_data(self, **kwargs):
        ctx = super(LoteCreateView, self).get_context_data(**kwargs)

        ctx['producto'] = Productos.objects.get(
                pk=self.request.GET.get('producto_id')
            )
        return ctx
        
    def form_valid(self, form):

        producto = Productos.objects.get(
            pk=self.request.GET.get('producto_id')
        )

        producto.Precio = form.cleaned_data.get('PrecioVenta')
        producto.save()

        return super(LoteCreateView, self).form_valid(form)

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

class PedidosCreateView(CreateView):
    model = Pedidos
    fields = [
        'Monto',
        'TipoPedido'
    ]
    template_name = 'inventario/pedido_create.html'
    success_url = reverse_lazy('listar_producto')
    #Contexto de productos
    def get_context_data(self, **kwargs):
        ctx = super(PedidosCreateView, self).get_context_data(**kwargs)

        ctx['productos'] = Productos.objects.all()
           
        return ctx

  
