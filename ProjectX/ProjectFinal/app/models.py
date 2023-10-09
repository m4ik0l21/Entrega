from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser, Group, Permission

class RegistroUsuarios(AbstractUser):
    email = models.EmailField()
    username = models.CharField(max_length=600, unique=True)
    password = models.CharField(max_length=600)
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    def __str__(self):
        return self.username

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class RegistroLuchadores(models.Model):
    nombre = models.CharField(max_length=600)
    edad = models.IntegerField()
    peso = models.FloatField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Luchador'
        verbose_name_plural = 'Luchadores'

class RegistroEmpresas(models.Model):
    nombre = models.CharField(max_length=600)
    direccion = models.CharField(max_length=600)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

class RegistroEvento(models.Model):
    nombre = models.CharField(max_length=600)
    fecha = models.DateField()
    horario = models.TimeField()
    lugar = models.CharField(max_length=600)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

class BuscarLuchadoresForm(forms.Form):
    query = forms.CharField(label='Nombre', max_length=100)

class BuscarEmpresasForm(forms.Form):
    query = forms.CharField(label='Nombre', max_length=100)

class BuscarEventosForm(forms.Form):
    query = forms.CharField(label='Nombre', max_length=100)