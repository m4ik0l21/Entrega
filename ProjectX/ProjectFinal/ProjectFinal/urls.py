from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.PaginaInicial, name='pagina_inicial'),
    path('admin/', admin.site.urls),
    path('Lucha-libre/', include('app.urls'))
]