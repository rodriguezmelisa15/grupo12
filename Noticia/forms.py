from django import forms
from .models import Noticia

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
