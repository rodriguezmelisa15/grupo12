from django.urls import path
from .views import HomeView, VistaEditarNoticia, VistaNuevaNoticia, VistaEliminarNoticia, VistaQuienesSomos,ComentarioNoticia,VistaDetalleNoticia, VistaMision,VistaLugarContacto

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('noticia/<int:pk>', VistaDetalleNoticia.as_view(), name='detalle-noticia'),
    path('crear_noticia/', VistaNuevaNoticia.as_view(), name='crear_noticia'),
    path('noticia/<int:pk>/eliminar/',
         VistaEliminarNoticia.as_view(), name='eliminar_noticia'),
    path('nosotros/', VistaQuienesSomos, name='nosotros'),
    path('noticia/<int:pk>/comentarios', ComentarioNoticia.as_view(), name='crear_comentario'),
    path('noticia/editar/<int:pk>', VistaEditarNoticia.as_view(), name = 'editar_noticia'),
    path('mision/', VistaMision , name='mision'),
    path('lugar_contacto/', VistaLugarContacto , name='lugar-contacto'),
    
    
    
]

