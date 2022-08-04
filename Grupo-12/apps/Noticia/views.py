from django.shortcuts import render
from .models import Noticia

def noticia(request):
    noti= Noticia.objects.all()
    return render(request,'noticia.html',{"noticia":noti})
