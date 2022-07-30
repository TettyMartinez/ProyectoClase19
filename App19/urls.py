from django.urls import path
from App19 import views
from App19.views import *

urlpatterns = [
    path('curso/', views.curso, name="Curso"),
    path('cursos/', views.cursos, name= 'cursos'),
    path('estudiantes/', views.estudiantes, name= 'estudiantes'),
    path('profesores/', views.profesores, name= 'profesores'),
    path('entregables/', views.entregables, name= 'entregables'),
    path('', views.inicio, name='Inicio'),
    #path('cursoFormulario/', views.cursoFormulario, name='CursoFormulario'),
    #path('profeFormulario/', views.profeFormulario, name='ProfeFormulario'),
    path('busquedaComision/', views.busquedaComision, name='BusquedaComision'),
    path('buscar/', views.buscar),
]
