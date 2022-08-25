from django.shortcuts import render,redirect
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate

"""class VistaRegistroVisitante(generic.CreateView):
    form_class= UserCreationForm
    template_name = 'Visitante/registro/registro.html'
    success_url = reverse_lazy('login')
"""
"""
def Create(request):
    usuario = request.POST['txtNickname']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    mail = request.POST['txtMail']
    contraseña = request.POST['txtContra']
    Usuario.objects.create(usuario= usuario, nombre= nombre, apellido= apellido, mail=mail, contraseña=contraseña,)
    return redirect('login/')
"""

def registro_usuario(request):
    data = {
        'form': CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm (request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
    


    return render(request,'Visitante/registro.html', data)
