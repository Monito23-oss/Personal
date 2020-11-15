from django.contrib import admin
from django.urls import path
from . import views # Estamos importando todo lo que esta en el archivo de views con el punto

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),#Es la forma que indicamos que estamos utilizando una vista generica.
    path('lista/', views.PruebaListView.as_view()),#Aqui utilizamos la url para llamar a nustra clase.
    path('lista_prueba/', views.ListarPrueba.as_view()),# Aqui utilizamos la url para llamar a nuestra clase del MOdelo.
    path('add/', views.PruebaCreaView.as_view()),# Aqui utilizamos la url para llamar a nuestra clase del CreateView.
    path('resume_foundation/', views.ResumenFoundationView.as_view()),# Aqui utilizamos la url para llamar a nuestra clase del CreateView.
]
