from django.shortcuts import render
from django.urls import reverse_lazy #Paquete para trabajar urls
#Vistas genericas django
from django.views.generic import(
    ListView, #Ayuda a listar los registros de un modelo o una base de datos.
    DetailView, #Ayuda a mostrar la informacion en detalle de un registro de un modelo
    CreateView, #Ayuda a registar informacion en un modelo o una base de datos
    TemplateView,
    UpdateView,#Ayuda a modificar informacion en un modelo o una base de datos
    DeleteView #Ayuda a eliminar informacion en un modelo o una base de datos
)
#Importacion de models
from .models import Empleado
#Importacion de forms
from .forms import EmpleadoForm
# Create your views here.
"""
Requerimientos del cliente
1) Listar todos los empleados de la empresa
2) Listar todos los empleados que pertenecen a una area de la empresa
3) Listar todos los empleados por trabajo
4) Listar los empleados por palabra clave
5) Listar habilidades de un empleado
"""
# 1 requerimiento
#vistas vasadas en clases
class ListTodosEmpleados(ListView):
    #Toda vista Django requiere un templeta con cual va a trabajar
    template_name = 'persona/list_todos.html'
    paginate_by = 4 #esto se utiliza para mostrar solo registro de 4
    ordering = 'id'
    context_object_name = 'empleados'
    #EL ListView requiere de un modelo
    #model = Empleado
    #Si estamo sobre escribiendo el metodo queryset ya no es necesario  escrbir el modelo arriba
    def get_queryset(self):
        palabra_clave = self.request.GET.get("Kword",'')
        #jorge = jo lo que contenga la iniciales es el icontains
        lista = Empleado.objects.filter(
            last_name__icontains=palabra_clave
            )
        return lista

# 2 requerimiento
#vistas vasadas en clases
class ListByAreaEmpleados(ListView):
    #Toda vista Django requiere un templeta con cual va a trabajar
    #Listar empleados de una area
    template_name = 'persona/list_by_area.html'
    context_object_name='empleados'
    """
    primera forma para traer la inforacion de un modelo con filtro
    #EL ListView requiere de un modelo
    queryset = Empleado.objects.filter( #Aqui vamos a filtrar la informacion del queryset
        departamento__shor_name = 'Contabilidad'
    """
    def get_queryset(self): #con esta parte estamos haciendo el mismo filtro
        area = self.kwargs['shorname']#aqui especificamos el valor de la url que queremos filtrar
        lista = Empleado.objects.filter(
            departamento__shor_name = area #Aqui hace el remplazo
            )
        return lista
#4) Listar los empleados por palabra clave
class ListEmpleadosByKword(ListView):
    """ Lista de empleados por palabara clave """
    template_name = 'persona/list_by_kword.html'
    context_object_name = 'Gente'
    #Aqui definimos filtro por palabre clave
    """
    def get_queryset(self):
         #Con estos comando vamos  a recupara la palabra clave del la peticion GET del recuadro Buscar
        print('---------------')
        palabra_clave = self.request.GET.get("kword",'')
        print('Palabra Clave',palabra_clave )
        print('---------------')
        return []
    """
    def get_queryset(self):
        palabra_clave = self.request.GET.get("Kword",'')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
            )
        print('*******')
        print('Empleados =',lista)
        print('*******')
        return lista
#5) Listar habilidades de un empleado
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    #Vamos a definir el queryset donde se va a procesar  la lista que queremos dar como resultado
    def get_queryset(self):
        #Vamos a acceder a un empleados
        empleado = Empleado.objects.get(id=3)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()
#Vamos a crear la vista para trabajar con el ListView
class EmpleadoDetailView(DetailView):
    #El DetailView necesita por obligacion un modelo
    #Ya que esta muestra los datos un registro
    model = Empleado
    template_name = 'persona/detail_empleado.html'
    #vamos a utilizar el metodo get_context_data para poner nuevas cosas en el template_name
    def get_context_data(self,**kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #Se pone Titulo en el template
        context['Titulo'] = 'Empleado del mes'
        return context

#Vamos a crear un template para redireccionar el los datos registrados en el CreateView
class SuccessView(TemplateView):
    template_name = 'persona/success.html'

#Vamos a crear la vista para trabajar con el CreateView
class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    #CreateView necesita un fields para poder Registrar los parametros
    #fields =['first_name','last_name','job']#Para registrar uno por uno ponemos el nombre entre comillas ''
    #fields = ('__all__')#Con esto especificamos registrar todos losr registros del modelo
    #Como trabajamos con los forms ponemos en comentario los fields
    """
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',

    ]
    """
    #Asignamos el modelo de forms
    form_class=EmpleadoForm
    #Se va a definir la URL que se redirecciona cuando se completa el registros
    #success_url = '.'#Aqui se redirecciona a la misma pagina.
    success_url = reverse_lazy('personas_app:Correcto')#Aqui se redirecciona a otra pagina creada con el 'name' especificado en l url

    #Vamos a utilizar esta clase para validar los registros de cada campo del CreateView
    def form_valid(self,form):
        #Logica del proceso
        #Asiganar la infomracion gurdada del CreateView a la variable empleado
        empleado = form.save(commit = False)#Recuperar una instancia del formulario vinculado en la base de datos
        #print(empleado) imprime en pantalla el nombre Completo
        empleado.full_name = empleado.first_name + ' '+ empleado.last_name #Aqui actualiza el campo del modelos que no son obligatorio llenar
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

#Vamos a crear un template para redireccionar el los datos registrados en el UpdateView
class ActulizarView(TemplateView):
    template_name = 'persona/actualizar.html'

class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    #Campos a actulizar
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',

    ]
    success_url = reverse_lazy('personas_app:Modificar_empleado')#Aqui se redirecciona a otra pagina creada con el 'name' especificado en l url


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('******metodo post****')
        print('*****')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('******metodo form_valid****')
        print('*****')
        return super(EmpleadoUpdateView, self).form_valid(form)

#Vamos a crear un template para redireccionar el los datos registrados en el DeleteView
class EliminarView(TemplateView):
    template_name = 'persona/eliminar.html'

class EmpleadoDeleteView(DeleteView):
    model= Empleado
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('personas_app:Eliminar_empleado')#Aqui se redirecciona a otra pagina creada con el 'name' especificado en l url
#-------------------------------------------------------------------------------------------------------------
#Inicio del proyecto
class InicioView(TemplateView):
    """Vista que carga pagina de inicio"""
    template_name = 'inicio.html'


class ListaEmpleadosAdmin(ListView):
    #Toda vista Django requiere un templeta con cual va a trabajar
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10 #esto se utiliza para mostrar solo registro de 4
    ordering = 'id'# como va ordenar los resultados
    context_object_name = 'empleados'#Palabra clave para recibir los datos en el template
    model = Empleado#Modelo de a donde recibe los registros
