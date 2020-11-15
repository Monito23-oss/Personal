from django.shortcuts import render
#Vistas genericas django
from django.views.generic import(
    ListView, #Ayuda a listar los registros de un modelo o una base de datos.
    DetailView, #Ayuda a mostrar la informacion en detalle de un registro de un modelo
    CreateView, #Ayuda a registar informacion en un modelo o una base de datos
    TemplateView,
    UpdateView,#Ayuda a modificar informacion en un modelo o una base de datos
    DeleteView #Ayuda a eliminar informacion en un modelo o una base de datos
)
#Vista generica que esta relacionada cunado no se trabajan con modelos directamente si no con varios
from django.views.generic.edit import FormView

from aplicaciones.personas.models import Empleado
from .models import Departamento

from .forms import NewDepartamentoForm
# Create your views here.
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self,form):
        print('***********Estamos en el form valid**********')
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        return super(NewDepartamentoView, self).form_valid(form)
#-------------------------------------------------------------------------------------------------------------
#Inicio del proyecto
class DepartamentoListView(ListView):
    """Vista que carga los departamentos"""
    template_name = 'departamento/lista.html'
    model = Departamento
    context_object_name = 'departamentos'
