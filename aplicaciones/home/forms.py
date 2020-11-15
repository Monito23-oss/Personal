from django import forms #Libreria para utilizar la formularios especialisados
#Codigo que conceta los modelos con la vista y se  ve en el html
#Importar modelos
from .models import Prueba

class PruebaForm(forms.ModelForm):
    class Meta:
        model = Prueba
        #fields = ("__all__")#Trae todos los campos del modelo y los manda a la vista del CreateView
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        #Vamos a personalisar los campos con widgets
        widgets ={
            'titulo':forms.TextInput(
                attrs = { #Atributos
                    'placeholder': 'Ingrese texto aqui'
                }
            )
        }
    #vamos a programar para que solo muestre cantidades menores o mayores a 10
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']# Recupera el valor de cantidades
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad
