from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleados1',
        'USER': 'ricardo11',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]#Direccion para indicar donde va a quedar los archivos estaticos

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')#Direccion para indicar donde va a quedar los archivos de multimedia que suban los registros de empleados
