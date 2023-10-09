from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def PaginaInicial(req):
    return render(req, 'Inicio.html')

def Registro_Usuarios(req):
    if req.method == "POST":
        formulario = RegistroUsuariosForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req, 'Inicio_Sesion.html')
    else:
        formulario = RegistroUsuariosForm()
    return render(req, 'Inicio.html', {'formulario': formulario})
def Inicio_Sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
            else:
                return render(request, 'template_inicio_incorrecto.html')
        else:
            return render(request, 'template_inicio_incorrecto.html')
    else:
        formulario = AuthenticationForm()
    return render(request, 'Inicio_Sesion.html', {'formulario': formulario})

def home(req):
    return render(req,'home.html')
def Registro_Luchadores(req):
    if req.method == "POST":
        formulario = LuchadorForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req,'home.html')
    else:
        formulario = LuchadorForm()
    return render(req,'Luchadores.html', {'formulario': formulario})

def Registro_Empresas(req):
    if req.method == "POST":
        formulario = EmpresaForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req,'home.html')
    else:
        formulario = EmpresaForm()
    return render(req,'Empresas.html', {'formulario': formulario})

def Registro_Eventos(req):
    if req.method == "POST":
        formulario = EventoForm(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req,'home.html')
    else:
        formulario = EventoForm()
    return render(req,'Eventos.html', {'formulario': formulario})

def buscar_luchador(req):
    form = BuscarLuchadoresForm(req.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        luchadores_list = RegistroLuchadores.objects.filter(nombre__icontains=query)
    else:
        luchadores_list = None
    return render(req,'Resultados_Busqueda_Luchadores.html', {'luchadores_list': luchadores_list, 'form': form})

def buscar_empresas(req):
    form = BuscarEmpresasForm(req.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        empresas = RegistroEmpresas.objects.filter(nombre__icontains=query)
    else:
        empresas = None
    return render(req,'Resultados_Busqueda_Empresas.html', {'empresas': empresas, 'form': form})

def buscar_eventos(req):
    form = BuscarEventosForm(req.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        eventos = RegistroEvento.objects.filter(nombre__icontains=query)
    else:
        eventos = None
    return render(req,'Resultados_Busqueda_Eventos.html', {'nombres_eventos': eventos, 'form': form})