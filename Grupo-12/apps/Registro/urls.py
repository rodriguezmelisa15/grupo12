from django import views
from django.urls import path
from .views import Registro


urlpatterns = [
    path('', Registro.as_view(), name="registro"),
    
]
