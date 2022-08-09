from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Noticia
from .forms import NoticiasForm
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
