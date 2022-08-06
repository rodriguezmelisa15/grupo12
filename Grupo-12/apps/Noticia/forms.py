from dataclasses import field
from django import forms
from .models import Noticia

class Noticiaform(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all___'

