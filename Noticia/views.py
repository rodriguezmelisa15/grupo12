from pickle import GET
import re
import string
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Noticia, Comment
from .forms import NoticiasForm, CrearComentario
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Noticia
    template_name = 'Noticia/home.html'
    context_object_name = "noticias"

    def get_queryset(self):
        
        if self.request.method=="GET" and "filtrado" in self.request.GET :
            if ((self.request.GET.get("select")) == "1" ):
                qs=Noticia.objects.all()
                categoria= self.request.GET.get("filtro")
                if categoria:
                    qs= qs.filter(categoria=categoria)
                    return qs
            elif ((self.request.GET.get("select")) == "2" ):
                qs=Noticia.objects.all()
                fecha= self.request.GET.get("filtro")
                if fecha:
                    qs= qs.filter(fecha_noticia=fecha)
                    return qs
        else:
            qs=Noticia.objects.all()
            return qs

class VistaDetalleNoticia(DetailView):
    model = Noticia
    template_name = 'Noticia/detalles_noticia.html'


class VistaNuevaNoticia(CreateView):
    model = Noticia
    form_class = NoticiasForm
    template_name = 'Noticia/crear_noticia.html'
    #fields = '__all__'


class VistaEliminarNoticia(DeleteView):
    model = Noticia
    template_name = 'Noticia/eliminar_noticia.html'
    success_url = reverse_lazy('home')


def VistaQuienesSomos(redirect):
    return render(redirect, 'Noticia/nosotros.html')


class ComentarioNoticia(CreateView):
    model = Comment
    form_class = CrearComentario
    template_name = 'Noticia/comentarios.html'
    #fields = '__all__'

    
    def form_valid(self, form):
        f = form.save(commit = False)
        f.noticia_id= self.kwargs['pk']
        f.usuario= self.request.user.username
        print(self.request.user.id)
        return super(ComentarioNoticia, self).form_valid(form)
        

    success_url = reverse_lazy('home')
