from django.urls import path
from .views import VistaRegistroVisitante, VistaLogin

urlpatterns = [
    path('users/', VistaRegistroVisitante.as_view(), name="registro"),
    path('login/', VistaLogin.as_view(), name="inicio-sesion"),
]
