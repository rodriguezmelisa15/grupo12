import mailbox
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .models import usuario



# Create your views here.

def registro(request):
    usuarios=usuario.objects.all()
    return render(request, "registro.html",{"user": usuarios})

def createUsuario(request):
    usuario= request.POST['txtUsuario']
    nombre= request.POST['txtNombre']
    apellido= request.POST['txtApellido']
    mail= request.POST['txtMail']
    contraseña= request.POST['txtContraseña']


    usuario= usuario.object.create(usuario=usuario, nombre= nombre, apellido= apellido, mail= mail, contraseña= contraseña)
    return redirect('/')