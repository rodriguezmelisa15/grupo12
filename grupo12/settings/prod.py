from .base import *

SETTINGFILES_DIRS = {
    os.path.join(os.path.dirname(BASE_DIR), "settings"),
}


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        'ENGINE': 'mssql',
        'NAME':'db65kq741noh2c',
        'USER': 'wxeumdtcmognir',
        'PASSWORD': '7d08c4a9c7ca74e5ab7ff6fb6bfcf4d7a3ca7e96d391e9b48a5c1400a3a3d7a2',
        'HOST': 'ec2-44-207-126-176.compute-1.amazonaws.com',
        'PORT': '5432',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}


