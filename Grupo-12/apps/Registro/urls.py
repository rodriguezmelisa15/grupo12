from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro),
    path('registro/',views.createUsuario),
]
