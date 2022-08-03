from django.db import models

# Create your models here.

class usuario(models.Model):
    usuario:models.CharField(primary_key=True,max_length=8)
    nombre:models.CharField(max_length=50)
    apellido:models.CharField(max_length=50)
    mail:models.CharField(max_length=50)
    contraseña:models.CharField(max_length=8)

def __str__(self):
    texto= '{0} ({1})'
    return texto.format(self.usuario, self.nombre)