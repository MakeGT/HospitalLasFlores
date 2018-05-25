from django.contrib import admin
from .models import Productos
from .models import Lotes
admin.sites.register(Productos)
admin.sites.register(Lotes)

# Register your models here.
