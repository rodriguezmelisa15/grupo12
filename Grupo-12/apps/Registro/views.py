from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Usuario
# Create your views here.

#def registro(request):
#    return render(request, "registro.html")

class Registro(ListView):
    model = Usuario
    template_name = 'registro.html'
