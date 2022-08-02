from .base import *
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'grupo12db',
        'USER': 'melisa',
        'PASSWORD':'melusa2012',
        'HOST': 'localhost\SQLEXPRESS',
        'PORT': '',
        'OPTIONS': {
            'driver':'ODBC Driver 17 for SQL Server',
            #'extra_params': "Persist Security Info=False;server=localhost\SQLEXPRESS\saludo",
        },
    }
}
