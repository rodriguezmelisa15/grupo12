from django.shortcuts import render,redirect
from .models import Usuario



def home (request):
    usuarios= Usuario.objects.all()
    return render(request,"registro.html",{"nuevo": usuarios})

def Create(request):
    usuario = request.POST['txtUsuario']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    mail = request.POST['txtMail']
    contraseña = request.POST['txtContra']
    
    Usuario.objects.create(usuario= usuario, nombre= nombre, apellido= apellido, mail=mail, contraseña=contraseña)
    return redirect('http://localhost:8000')
    