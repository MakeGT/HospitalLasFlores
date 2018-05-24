from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView,
    DateDetailView,
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
        'Existencia'
    ]
    template_name = 'inventario/productos_create.html'
    #success_url = reverse_lazy('productos_lista')

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
        'Existencia'
    ]

    template_name = 'productos/productos_create.html'
    success_url = reverse_lazy('productos_lista')