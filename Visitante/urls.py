from unicodedata import name
from django.urls import path
from .views import registro_usuario


urlpatterns = [
    #path('registro/',views.Create),
    path('registro/',registro_usuario , name='registro_usuario'),
  
]