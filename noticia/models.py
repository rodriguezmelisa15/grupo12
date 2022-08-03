from django.db import models
from django.contrib.auth.models import User 

class Noticia(models.Model):
    titulo = models.CharField(max_length = 255)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    cuerpo = models.TextField()
<<<<<<< Updated upstream:noticia/models.py
=======
    
    
>>>>>>> Stashed changes:Grupo-12/apps/Noticia/models.py

    def __str__(self):
        return self.titulo +' | '+ str(self.autor)

