from django.urls import path
from .views import HomeView, VistaDetalleNoticia, VistaNuevaNoticia, VistaEliminarNoticia, VistaQuienesSomos

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name="home"),
    path('noticia/<int:pk>', VistaDetalleNoticia.as_view(), name='detalle-noticia'),
    path('crear_noticia/', VistaNuevaNoticia.as_view(), name='crear_noticia'),
    path('noticia/<int:pk>/eliminar/',
         VistaEliminarNoticia.as_view(), name='eliminar_noticia'),
    path('nosotros/', VistaQuienesSomos, name='nosotros')
]
