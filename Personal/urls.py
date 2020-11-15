"""Personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#Vamos a incluir las librerias re_path para traer urls de la carpeta aplicaciones
#departamentos y include para indicarle la direccion de donde traer.
from django.urls import re_path, include
#Vamos a importar la carpeta para traer los archivos multimedia
from django.conf import settings
#Paquete para generar url estaticas
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('aplicaciones.departamento.urls')),
    re_path('',include('aplicaciones.personas.urls')),
    re_path('',include('aplicaciones.home.urls'))
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#Esto tiene que ver con los archivos de multimedia que se suban
