from django.urls import path
from .views import VistaRegistroVisitante

urlpatterns = [
    path('registro/', VistaRegistroVisitante.as_view(), name="registro"),
    
]