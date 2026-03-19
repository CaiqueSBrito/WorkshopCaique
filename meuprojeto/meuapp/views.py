from django.shortcuts import render
from rest_framework import viewsets
from .models import Pokemon
from .serializers import PokemonSerializer
from django.http import HttpResponse

def home(request):
    return render(request, 'meuapp/index.html')
    
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

def pokemon_list(request):
    return render(request, 'meuapp/api_teste.html')
     
def tutorial(request):
    return render(request, 'meuapp/tutorial.html')