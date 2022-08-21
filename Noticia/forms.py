from django import forms
from .models import Noticia, Comment

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'categoria', 'autor', 'cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte un titulo a la noticia'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control','placeholder': 'Nombre del autor'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placerholder':'cuerpo de la noticia'}),
        }

class CrearComentario(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('usuario', 'comentario')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'titulo_cartel': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control','placeholder': 'Nombre del autor'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'placerholder':'comentario'}),
        }
        
