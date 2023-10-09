from django.contrib import admin
from app.models import RegistroLuchadores, RegistroEmpresas, RegistroEvento, RegistroUsuarios

class RegistroUsuariosAdmin(admin.ModelAdmin):
    list_display = ['email', 'username','password']
    list_filter = ['email', 'username','password']
    search_fields = ['email', 'username','password']

class RegistroLuchadoresAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'edad', 'peso']
    list_filter = ['nombre', 'edad', 'peso']
    search_fields = ['nombre', 'edad', 'peso']

class RegistroEmpresasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono']
    list_filter = ['nombre', 'direccion', 'telefono']
    search_fields = ['nombre', 'direccion', 'telefono']

class RegistroEventoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'horario', 'lugar']
    list_filter = ['nombre', 'fecha', 'horario', 'lugar']
    search_fields = ['nombre', 'fecha', 'horario', 'lugar']

admin.site.register(RegistroUsuarios, RegistroUsuariosAdmin)
admin.site.register(RegistroLuchadores, RegistroLuchadoresAdmin)
admin.site.register(RegistroEmpresas, RegistroEmpresasAdmin)
admin.site.register(RegistroEvento, RegistroEventoAdmin)