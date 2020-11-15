from django.db import models
#Vamos a importar el modelo Departamento de la aplicacion Departamento
#Importamos la ubicacion exacata de la carpeta
from aplicaciones.departamento.models import Departamento
#Importacion de apliciones de terceros
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    #Cada empleado va atener un conjunto de habilidades
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad' #Cambia el nombre del moedelo pero con la s al final y en el menu cuando se escoje
        verbose_name_plural= 'Habilidades de cada empleado'# Cambia el nombre de la clase completo  En la parte Izquierda del administradoe

    def __str__(self):
        return str(self.id) + '-' + self.habilidad #str(self.id) este comondo nos va a mostrar el numero del registro

# Create your models here.
class Empleado(models.Model):
    #Modelo para  nuestra tabla Empleado
    #Contador
    #Administrador
    #Economista
    #Otro
    Job_choice = ( #Se va a guardar en el registro lo que es la primera columna
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    first_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('Apellidos',max_length=60)
    full_name = models.CharField('Nombre Completo',max_length=100, blank =True)
    job = models.CharField('Trabajo',max_length=60,choices=Job_choice) #choices nos va permitir registrar una entrada pero que se de selecion unicada
    departamento = models.ForeignKey(Departamento , on_delete=models.CASCADE)#Aqui utilizamos el modelo que importamos para el ForeignKey
    avatar = models.ImageField(upload_to='empleado', blank= True, null=True)#Campo para Subir una imagen
    habilidades = models.ManyToManyField(Habilidades)#Aqui vamos a especificar con cual relacion de modelos mucho a mucho se quiere trabajar
    hoja_de_vida = RichTextField()#Aqui se va ytilizar la aplicacion de terceros.

    class Meta:
        verbose_name = 'Pesonal General' #Cambia el nombre del moedelo pero con la s al final y en el menu cuando se escoje
        verbose_name_plural= 'Personal de la empresa'# Cambia el nombre de la clase completo  En la parte Izquierda del administradoe
        ordering = ['-first_name', 'last_name'] #Estas es la forma de organizar los registor del modelo Departamento por orden como se desee.
        unique_together=('first_name', 'last_name') #Esto indica que no se repitan los registros

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name #str(self.id) este comondo nos va a mostrar el numero del registro
