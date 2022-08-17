from django import forms
from .models import Noticia, Comment

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'titulo_cartel', 'autor', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte un titulo a la noticia'}),
            'titulo_cartel': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control','placeholder': 'Nombre del autor'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placerholder':'cuerpo de la noticia'}),
        }
<<<<<<< HEAD
<<<<<<< Updated upstream
=======
=======
>>>>>>> 182aa09eb838b8c89cf9bcb17091a752aacf5e60

class CrearComentario(forms.ModelForm):
    class Meta:
        model = Comment
<<<<<<< HEAD
        fields = ('usuario', 'comentario')
=======
        fields = ('comentario',)
>>>>>>> 182aa09eb838b8c89cf9bcb17091a752aacf5e60

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'titulo_cartel': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control','placeholder': 'Nombre del autor'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'placerholder':'comentario'}),
        }
        
<<<<<<< HEAD
>>>>>>> Stashed changes
=======
>>>>>>> 182aa09eb838b8c89cf9bcb17091a752aacf5e60
