from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from App19.models import Curso
# Create your views here.

def curso(self):
    curso= Curso(nombre="Desarrollo web", comision=1)
    curso.save()
    doc_texto= f"Curso: {curso.nombre}      Comision: {curso.comision}"

    return HttpResponse(doc_texto)


def inicio(request):
    return render(request,'App19/inicio.html')

def cursos(request):
    return render(request,"App19/cursos.html")

def profesores(request):
    return render(request,'App19/profesores.html')

def estudiantes(request):
    return render(request,'App19/estudiantes.html')

def entregables(request):
    return render(request, 'App19/entregables.html')