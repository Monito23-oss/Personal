
from django.contrib import admin
from django.urls import path
from . import views # Estamos importando todo lo que esta en el archivo de views con el punto

app_name = "personas_app"#Esto sirve para utilizar las url mas facilmente

urlpatterns = [
     path('listar-todos-empleados/', views.ListTodosEmpleados.as_view(),name='empleados_all'),#Es la forma que indicamos que estamos utilizando una vista generica.
     #Vamos utilizar un valor en la url para hcer el filtro
     path('listar-by-area/<shorname>/', views.ListByAreaEmpleados.as_view(),name='empleados_area'),#Es la forma que indicamos que estamos utilizando una vista generica.
     path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),#Es la forma que indicamos que estamos utilizando una vista generica.
     path('listar-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),#Es la forma que indicamos que estamos utilizando una vista generica.
     #El pk es obligatorio para mostrar el DetailView De un registro ya que este es el id
     path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(),name='empleados_detail'),#Es la forma que indicamos que estamos utilizando una vista generica.
     path('registrar-empleado/', views.EmpleadoCreateView.as_view(),name = 'agregar_new_empleado'),#Es la forma que indicamos que estamos utilizando una vista generica.
     path(
         'success/',
         views.SuccessView.as_view(),
         name='Correcto'),#Es la forma que indicamos que estamos utilizando una vista generica.
    #Url para UpdateView
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(),name='modificar_empleado'),#Es la forma que indicamos que estamos utilizando una vista generica.
    path(
        'Actulizacion/',
        views.ActulizarView.as_view(),
        name='Modificar_empleado'),#Es la forma que indicamos que estamos utilizando una vista generica.
    #Url para DeleteView
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(),name='eliminar_empleado'),#Es la forma que indicamos que estamos utilizando una vista generica.
    path(
        'Eliminar/',
        views.EliminarView.as_view(),
        name='Eliminar_empleado'),#Es la forma que indicamos que estamos utilizando una vista generica.

        #-----------------------------------------------------------------------------------------------
        #Creacion de proyecto

        path(
            '',#No ponemos nada po rque quermos que entre directo con http://127.0.0.1:8000
            views.InicioView.as_view(),
            name='inicio'),#Es la forma que indicamos que estamos utilizando una vista generica.

        path('listar-empleados-admin/',
         views.ListaEmpleadosAdmin.as_view(),
         name='empleados_admin'),#Es la forma que indicamos que estamos utilizando una vista generica.




 ]
