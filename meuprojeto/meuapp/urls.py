from django.urls import path, include
from meuapp import views

urlpatterns = [
    path('index/', views.home, name='home'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
]