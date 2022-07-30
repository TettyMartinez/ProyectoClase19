from django import forms

class CursoFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    comision=forms.IntegerField()

class ProfeFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=40)