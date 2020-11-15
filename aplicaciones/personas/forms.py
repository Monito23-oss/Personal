#Importacion para utilizar los archivos forms
from django import forms
#Importacion del modelo
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
     class Meta:
         model= Empleado
         fields=(
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
          )
         widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
