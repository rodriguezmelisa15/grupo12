from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

Noticia_categoria=[
	(1,'Cursos'),
	(2,'Informacion'),
	(3,'Ingresos'),
]
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.IntegerField(
	    null=False, blank=False,
	    choices= Noticia_categoria,
	    default=1
    )
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha_noticia = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('home')

        
class Comment(models.Model):
    noticia = models.ForeignKey(Noticia, related_name="comentarios", on_delete=models.CASCADE)
    usuario = models.CharField(max_length=255)
    comentario = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.noticia.titulo, self.usuario)