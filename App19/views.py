from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from App19.models import Curso
# Create your views here.

def curso(self):
    curso= Curso(nombre="Desarrollo web", comision=1)
    curso.save()
    doc_texto= f"Curso: {curso.nombre}      Comision: {curso.comision}"

    return HttpResponse(doc_texto)
    