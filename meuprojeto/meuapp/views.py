from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, pokemon_facts

def home(request):
    return render(request, 'meuapp/index.html')
# Create your views here.

def listar_usuarios(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'meuapp/listar_usuarios.html', {'pessoas': pessoas})
