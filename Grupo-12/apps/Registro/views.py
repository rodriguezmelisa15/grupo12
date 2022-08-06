from django.shortcuts import render,redirect
from .models import Usuario



def home (request):
    return render(request,"registro.html")

def Create(request):
    usuario = request.POST['txtUsuario']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    mail = request.POST['txtMail']
    contraseña = request.POST['txtContra']

    Usuario.objects.create(usuario= usuario, nombre= nombre, apellido= apellido, mail=mail, contraseña=contraseña,)
    return redirect('/noticia/')
    


