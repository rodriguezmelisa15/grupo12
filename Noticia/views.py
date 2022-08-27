from pickle import GET
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Noticia, Comment
from .forms import NoticiasForm, CrearComentario, EditarNoticiasForm
from django.urls import reverse, reverse_lazy



class HomeView(ListView):
    model = Noticia
    template_name = 'Noticia/home.html'
    context_object_name = "noticias"

    def get_queryset(self):
        if self.request.method == "GET" and "filtrado" in self.request.GET:
            qs = Noticia.objects.all()
            categoria = self.request.GET.get("filtro")
            fecha = self.request.GET.get("date")
            if categoria:
                qs = qs.filter(categoria=categoria)
                if fecha:
                    qs=qs.filter(fecha_noticia=fecha)
                return qs
            if fecha:
                    qs = qs.filter(fecha_noticia=fecha)
                    return qs
            if ((self.request.GET.get("filtro")) == "" and (self.request.GET.get("date")=="")):
                qs = Noticia.objects.all()
                return qs 
        else:
            qs = Noticia.objects.all()
            return qs

class VistaDetalleNoticia(DetailView):
    model = Noticia
    template_name = 'Noticia/detalles_noticia.html'

class VistaNuevaNoticia(CreateView):
    model = Noticia
    form_class = NoticiasForm
    template_name = 'Noticia/crear_noticia.html'
        #fields = '__all__'

    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor = self.request.user
        print(self.request.user.username)
        return super(VistaNuevaNoticia, self).form_valid(form)



        

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
        f = form.save(commit=False)
        f.noticia_id = self.kwargs['pk']
        f.usuario = self.request.user.username
        print(self.request.user.id)
        return super(ComentarioNoticia, self).form_valid(form)

    def get_success_url(self):
        return reverse('detalle-noticia', kwargs={'pk': self.object.noticia_id})
    
    
    #success_url = reverse_lazy('home')
    

class VistaEditarNoticia(UpdateView):
    model = Noticia
    form_class = EditarNoticiasForm
    template_name = 'Noticia/editar_noticia.html'
    #fields = ['titulo', 'categorias', 'cuerpo']

    
def VistaMision(redirect):
    return render(redirect, 'Noticia/mision.html')

def VistaLugarContacto(redirect):
    return render(redirect, 'Noticia/lugar_contacto.html')

