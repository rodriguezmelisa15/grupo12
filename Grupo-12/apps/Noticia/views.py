#from msilib.schema import ListView
#from re import template
from django.shortcuts import render
from .models import Noticia
#from .forms import Noticiaform
from django.views.generic import ListView, DetailView

# def noticia(request):
    # formulario = Noticiaform (request.Post or None)
    # noticia= Noticia.objects.all()
    # return render(request,'noticia.html',{"noticia":noticia}, {'formulario': formulario})

class Noticias(ListView):
    model = Noticia
    template_name = 'noticia.html'

