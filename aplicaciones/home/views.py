from django.shortcuts import render
#Vamos a importar una vista que django tiene por defecto genericar(TemplateView)
from django.views.generic import TemplateView
#vamos a importar una vista que permite trbajar con elementos que son listables
from django.views.generic import ListView
#vamos a importar una vista que permite trabajar con elementos para crear un registro sobre el
#Un modelo de base de datos
from django.views.generic import CreateView
#Vamos a importar los modelos del archivo models.py
from .models import Prueba
#Importacion para .formularios
from .forms import PruebaForm
# Create your views here.
class PruebaView(TemplateView):
    #Aqui ponemos el mensaje que queremos ver en pantalla
    template_name ='home/prueba.html'# Toca ser especifico en las rutas donde se encuentra el templates

class ResumenFoundationView(TemplateView):
    #Aqui ponemos el mensaje que queremos ver en pantalla
    template_name ='home/resumen_foundation.html'# Toca ser especifico en las rutas donde se encuentra el templates

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    #vamos a pasar directamente una lista de strings
    context_object_name= 'listaNumeros'#Este se utiliza para definir la variable del queryset y poder monstrarlo en el templates
    queryset = ['10','20','30','40','50','60','70','80','90','100','200','300']#El queryset va ser referencia a una lista

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'#ruta que indica el archivo del tamplate
    model = Prueba #Aqui hacemos referencia a la tabal de que tenemos el archivo modeles.
    context_object_name = 'lista' #accedemos a los resultados de listar los resultados del modelo

class PruebaCreaView(CreateView):
    template_name = 'home/add.html'#ruta que indica el archivo del tamplate
    model = Prueba #Aqui hacemos referencia a la tabal de que tenemos el archivo modeles.
    #fields = ['titulo','subtitulo','cantidad' ]#Aqui idicamos que registros queremos crear de nuestro modelo
    form_class = PruebaForm # Formulario que trae los registros que queremos crear de nuestro modelo estos remplaza el atributo filds
    success_url = '/'#Aqui se redireciona al http://127.0.0.1:8000/
