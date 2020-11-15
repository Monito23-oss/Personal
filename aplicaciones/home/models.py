from django.db import models

# Create your models here.
class Prueba(models.Model):
    #Aqui vamos a escribir nuestros atributos del modelos
    #esto es una tabla de base de datos
    titulo = models.CharField(max_length=60)#Aqui definimos los atributos y los tipos
    subtitulo = models.CharField(max_length=60)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo # ''+ self.subtitulo #Esto es lo que va a retornar nuestro modelo en la consulta
