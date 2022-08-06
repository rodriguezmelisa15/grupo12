from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User 


class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 255, verbose_name='Titulo')
    autor = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Autor')
    #imagen = models.ImageField(upload_to = 'imagenes/',verbose_name= 'Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripcion', null=True)

    

    def __str__(self):
        return self.titulo +' | '+ str(self.autor)

    def delete(self, using = None, keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()



