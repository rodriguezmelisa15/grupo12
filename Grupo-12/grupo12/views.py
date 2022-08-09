from django.shortcuts import render
from apps.Noticia.models import Noticia


def inicio(request):
    noti= Noticia.objects.all()
    return render(request,'noticia.html',{"noticia":noti})