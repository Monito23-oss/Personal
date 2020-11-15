from django import forms #Libreria para utilizar la formularios especialisados
#Codigo que conceta los modelos con la vista y se  ve en el html
#Importar modelos


class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length = 50)
    apellidos = forms.CharField(max_length = 50)
    departamento = forms.CharField(max_length = 50)
    shorname = forms.CharField(max_length = 50)
