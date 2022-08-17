from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Noticia, Comment
from .forms import NoticiasForm,CrearComentario
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Noticia
    template_name = 'home.html'
    ordering = ['-fecha_noticia']


class VistaDetalleNoticia(DetailView):
    model = Noticia
    template_name = 'detalles_noticia.html'


class VistaNuevaNoticia(CreateView):
    model = Noticia
    form_class = NoticiasForm
    template_name = 'crear_noticia.html'
    #fields = '__all__'


class VistaEliminarNoticia(DeleteView):
    model = Noticia
    template_name = 'eliminar_noticia.html'
    success_url = reverse_lazy('home')


def VistaQuienesSomos(redirect):
    return render(redirect, 'nosotros.html')


class ComentarioNoticia(CreateView):
    model = Comment
    form_class = CrearComentario
    template_name = 'detalles_noticia.html'
    #fields = '__all__'
    """def form_valid(self, form):
        form.instance.noticia_id = self.kwargs['pk']
        return super().form_valid(form)"""
    success_url = reverse_lazy('home')

