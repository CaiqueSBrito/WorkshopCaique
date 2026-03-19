from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pokemons', views.PokemonViewSet, basename='pokemon')

urlpatterns = [
    path('index/', views.home, name='home'),
    path("api/pokemons/", views.PokemonViewSet.as_view({'get': 'list'}), name="buscar_pokemon"),
    path('api/', include(router.urls)),
    path('pokemons/all/', views.pokemon_list, name='pokemon_list'),
    path('tutorial/', views.tutorial, name='tutorial'),
]