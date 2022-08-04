from django.shortcuts import render, redirect
from .models import Usuario




# Create your views here.

def registro(request):
    prueba=Usuario.objects.all()
    return render(request, "registro.html",{"user": prueba})

def createUsuario(request):
    usuario= request.POST['txtUsuario']
    nombre= request.POST['txtNombre']
    apellido= request.POST['txtApellido']
    mail= request.POST['txtMail']
    contraseña= request.POST['txtContra']

    nuevo = Usuario.objects.create(
        usuario=usuario, nombre=nombre, apellido= apellido, mail= mail, contraseña= contraseña)
    return redirect('/')
    

