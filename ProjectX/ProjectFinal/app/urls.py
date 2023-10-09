from django.urls import path
from app import views

urlpatterns = [
    path('', views.PaginaInicial, name="PaginaInicial"),
    path('Inicio_Sesion/', views.Inicio_Sesion, name='Inicio_Sesion'),
    path('home/', views.home, name='home'), 
    path('Registro_luchador/', views.Registro_Luchadores, name='Registro_Luchadores'),
    path('Registro_empresa/', views.Registro_Empresas, name='Registro_Empresas'),
    path('RegistroEvento/', views.Registro_Eventos, name='Registro_Eventos'),
    path('buscar_luchador/', views.buscar_luchador, name='buscar_luchador'),
    path('buscar_empresas/', views.buscar_empresas, name='buscar_empresas'),
    path('buscar_eventos/', views.buscar_eventos, name='buscar_eventos'),
    path('Registro-usuarios/', views.Registro_Usuarios, name='Registro_Usuarios'),
]