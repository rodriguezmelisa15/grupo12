from django.shortcuts import render
from .models import Noticia

def noticia(request):
    noticia= Noticia.objects.all()
    return render(request,'noticia.html',{"noticia":noticia})

