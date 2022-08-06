from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(User,max_length=8, null = True)
    nombre = models.CharField(max_length=50, null = True)
    apellido = models.CharField(max_length=50, null = True)
    mail = models.CharField(max_length=50, null = True)
    contrasenia = models.CharField(max_length=8, null = True)


    def __str__(self):
        texto= '{0} ({1})'
        return texto.format(self.usuario, self.nombre)

        