from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy


class VistaRegistroVisitante(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'users/registro.html'
    success_url = reverse_lazy('login')


class VistaLogin(generic.CreateView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')
