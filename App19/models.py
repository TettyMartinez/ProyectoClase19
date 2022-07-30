from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    def __str__(self):
        return self.nombre+" "+str(self.comision)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField( )

    def __str__(self):
        return self.nombre+" "+str(self.apellido)

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField ( )
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre+" "+str(self.apellido)+ " "+str(self.profesion)

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_entrega = models.DateField ()
    entregado = models.BooleanField ()

    def __str__(self):
        return self.nombre+" "+str(self.fecha_entrega)+" "+str(self.entregado)