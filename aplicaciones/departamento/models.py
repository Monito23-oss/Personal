from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre',max_length=50, blank=True)# (Nombre) como va a figurar en el administrador django con el blank= true significa que puede mandar un espacio vacio en el registro
    #editable=False No muestra este campo en el administradro django
    shor_name = models.CharField('Nombre Corto',max_length=30, unique = True)# Unique sirve para que no se repitan los registros
    anulate = models.BooleanField('Anulado',default=False)#Datos de tipo booleano, por default el booleano sera falso

    class Meta:
        verbose_name = 'Mi Depertamento' #Cambia el nombre del moedelo pero con la s al final y en el menu cuando se escoje
        verbose_name_plural= 'Areas de la empresa'# Cambia el nombre de la clase completo  En la parte Izquierda del administradoe
        ordering = ['-name'] #Estas es la forma de organizar los registor del modelo Departamento por orden como se desee.
        unique_together=('name', 'shor_name') #Esto indica que no se repitan los registros

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name
