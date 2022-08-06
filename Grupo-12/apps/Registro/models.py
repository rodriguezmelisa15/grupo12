from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario= models.CharField(primary_key=True,max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    contraseña = models.CharField( max_length=16)
