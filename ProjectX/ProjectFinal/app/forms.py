from django import forms
from .models import *

class RegistroUsuariosForm(forms.ModelForm):
    class Meta:
        model = RegistroUsuarios
        fields = ('email', 'username', 'password')

class LoginForm(forms.ModelForm):
    class Meta:
        model = RegistroUsuarios
        fields = ('username', 'password')

class LuchadorForm(forms.ModelForm):
    class Meta:
        model = RegistroLuchadores
        fields = ('nombre', 'edad', 'peso')

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = RegistroEmpresas
        fields = ('nombre', 'direccion', 'telefono')

class EventoForm(forms.ModelForm):
    class Meta:
        model = RegistroEvento
        fields = ('nombre', 'fecha', 'horario', 'lugar')