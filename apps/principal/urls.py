from django.conf.urls import url,include
from apps.principal.views import index

urlpatterns =[
    url(r'^$', index, name= "principal"),
]