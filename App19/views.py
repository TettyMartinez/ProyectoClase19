from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from App19.models import *
import datetime
from App19.forms import *
from App19 import *
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

def cursos(request):
    if (request.method == 'POST'):
        miFormulario= CursoFormulario(request.POST)
        print (miFormulario)
        if miFormulario.is_valid:
            info= miFormulario.cleaned_data
            nombre= info["nombre"]
            comision= info["comision"]
            curso= Curso (nombre=nombre, comision=comision)
            curso.save()
            return render(request, "App19/inicio.html")
    else:
        miFormulario= CursoFormulario()
    return render(request, "App19/cursos.html", {"miFormulario":miFormulario})

def profesores(request):
    if (request.method == 'POST'):
        miFormulario= ProfeFormulario(request.POST)
        print (miFormulario)
        if miFormulario.is_valid:
            info= miFormulario.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profe= Profesor (nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render(request, "App19/inicio.html")
    else:
        miFormulario= ProfeFormulario()
    return render(request, "App19/profesores.html", {"miFormulario":miFormulario})

def busquedaComision(request):
    return render(request, "App19/busquedaComision.html")

def buscar(request):
    if request.GET["comision"]:
        comision=request.GET['comision']
        cursos= Curso.objects.filter(comision_incontains=comision)
        return render (request, "App19/resultadosBusqueda.html", {"cursos":cursos, "comision":comision})

    else:
            respuesta= f"No se han ingresado datos"
    return HttpResponse(respuesta)

