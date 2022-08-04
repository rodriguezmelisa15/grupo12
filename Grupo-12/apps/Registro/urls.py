from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro),
    path('createUser/',views.createUsuario),
]
