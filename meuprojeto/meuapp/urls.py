from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.home, name='home'),
    path("api/pokemons/", views.ver_pokemon, name="buscar_pokemon")
]