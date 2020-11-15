from django.contrib import admin
from .models import Empleado #Aqui registramos nuestro modelo para poder interactuar con el
from .models import Habilidades
# Register your models here.
admin.site.register(Habilidades)

#Decorador para clases mediante el administrador django
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        #vamos a incluir un campo mas que no se encuntra estipulado en el modelo
        'nombre_completo',
        'id',
    )

#Vamos a incluir un filtro para poder acceder mas facil a la informacion de la base de Datos
    search_fields = ('first_name',)
#Vamos a incluir un filtro para ver un cuadro a la derecha del administrador djangoproject
    list_filter = ('job','habilidades','departamento',)
#Vamos a poner un filtro especial para relacion de modelos muchos a muchos
    filter_horizontal = ('habilidades',)
#Aqui vamos a crear la funcion especial para dara valor a full_name
    def nombre_completo(self,obj): #Asi se pone una funcion especial para una clase extra en el decorador del Administrador , el object es el que permite traer los resultados de la clase
        #Vamos a definir toda la funcion
        #print(obj.id) #Aqui va a mostrar en consola el self del modelo Empleado (ojo) o los que el usuario defina
        return obj.first_name+' '+obj.last_name
    def id(self,obje):
        return obje.id

#Aqui tambien registramos el decorador de modelos por el Administrador(siempre debajo del decorador el modelo y el nombre del decrodor)
admin.site.register(Empleado, EmpleadoAdmin)
