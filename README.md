TRABAJO FINAL: GRUPO 12 
En este proyecto realizamos una pagina web de tipo blog
A continuacion detallaremos las instrucciones para obtener una copia del proyecto correctamente


Pre-requisitos 📋
asgiref                3.5.2
Django                 4.0.7
django-ckeditor        6.5.0
Pillow                 9.2.0
pyodbc                 4.0.34


Archivos gitignore 📄
El archivo que se encuntra con gitignore es local.py, el cual nos permite conectarnos a la base de datos, en nuetro caso es sql server managment,
por lo tanto dentro de nuestro archivo local tenemos el siguente codigo:

from .base import *
SETTINGFILES_DIRS = {
    os.path.join(os.path.dirname(BASE_DIR), "settings"),
}

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME':'', # nombre de la base de datos
        'USER': '', # usuario
        'PASSWORD': '', #contraseña
        'HOST': 'localhost\SQLEXPRESS',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}


Construido con 🛠️
- python
- html
- css
- visual studio code
- sql server managment 

Autores ✒️
- Enzo Steiner
- Federico Fogar
- Melisa Rodriguez
- Marcos Eguiazabal



