from pickle import GET
import re
import string
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Noticia, Comment
from .forms import NoticiasForm, CrearComentario
from django.urls import reverse_lazy

from django.template import loader
from django.http import HttpResponse


class HomeView(ListView):
    model = Noticia
    template_name = 'Noticia/home.html'
    ordering = ['-fecha_noticia']
    context_object_name = "noticia"

    def get_queryset(self):
        if self.request.method=="GET" and "filtrado" in self.request.GET :
            #print(self.request.GET.get("filtro"))
            
            if (self.request.GET.get("filtro") =='Cursos') or (self.request.GET.get("filtro") =='Informacion') or (self.request.GET.get("filtro") =='Ingresos'):
                consulta = Noticia.objects.filter(categoria=1)
                #template = loader.get_template('Noticia/home.html')
                context = {
                'noticia': consulta
                }
            print(self.request.GET.get("filtro"))        
        
        return super().get_queryset()


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





def VistaCompleta(request):
    from django.shortcuts import render
    from .models import Noticia
    from .models import Comment

    noticia= Noticia.objects.all()
    comentario = Comment.objects.all()

    return render(request, 'Noticia/detalles_noticia.html.html', {'noticia': noticia,'comentarios':comentario})










class ComentarioNoticia(CreateView):
    model= Noticia
    model = Comment
    form_class = CrearComentario

    template_name = 'Noticia/comentarios.html'
    #fields = '__all__'
    """
    def form_valid(self, form):
        form.instance.noticia_id = self.kwargs['pk']
        return super().form_valid(form)
    #success_url = reverse_lazy('home')
    """
    """
    def form_valid(self, form):
        f = form.save(commit = False)
        f.noticia_id= self.kwargs['pk']
        f.usuario_id= self.request.user
        return super(ComentarioNoticia, self).form_valid()
     """  
success_url = reverse_lazy('')
