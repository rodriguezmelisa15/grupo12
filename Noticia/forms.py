from django import forms
from .models import Noticia, Comment
from django.contrib.auth.models import User

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'categoria','cuerpo','imagen')


        def __init__(self, is_staff, *args, **kwargs):
            super(NoticiasForm, self).__init__(*args, **kwargs)
            self.fields["autor"].queryset=User.objects.all().exclude(is_staff==False)

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte un titulo a la noticia ##'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            #'autor': forms.Select(attrs={'class': 'form-control','placeholder': 'Nombre del autor'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placerholder':'cuerpo de la noticia'}),
        }

class CrearComentario(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comentario']

        widgets = {
            #'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            #'titulo_cartel': forms.TextInput(attrs={'class': 'form-control', }),
            #'autor': forms.Select(attrs={'class': 'form-control','placeholder': 'Nombre del autor'}),
            'comentario': forms.Textarea(attrs={'cols':"100",'rows':"5",'class': 'form-control', 'placerholder':'Comentario'}),
            #'noticia_id': forms.IntegerField({'placerholder':'noticia_id'}),
        }
        
class EditarNoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'categoria', 'cuerpo','imagen')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte un titulo a la noticia'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'placeholder': 'ingrese una categoria...'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placerholder':'cuerpo de la noticia'}),

        }

