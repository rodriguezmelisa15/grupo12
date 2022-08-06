from django.shortcuts import render
from .models import Noticia
from apps.Registro.models import Usuario

def noticia(request):
    noti= Noticia.objects.all()
    return render(request,'noticia.html',{"noticia":noti})

def home (request):
    usua= Usuario.objects.all()
    return render(request,'noticias.html',{"nuevo": usua})
