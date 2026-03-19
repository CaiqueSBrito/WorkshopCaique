import os
import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, pokemon_facts
from .forms import PessoaForm
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('API_KEY')

def home(request):
    return render(request, 'meuapp/index.html')
# Create your views here.

import requests # Se der erro, rode 'pip install requests' no terminal
from django.http import JsonResponse

def buscar_fato_api(request):
    url = os.getenv('API_KEY')
    
    if not url:
        return JsonResponse({'error': 'A variável API_KEY não foi encontrada no .env'}, status=500)
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        return JsonResponse(data, safe=False)
        
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Erro na chamada da API: {str(e)}'}, status=500)
    except Exception as e:
        return JsonResponse({'error': f'Erro genérico: {str(e)}'}, status=500)
                            
def listar_usuarios(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'meuapp/listar_usuarios.html', {'pessoas': pessoas})

def listar_pokemon_facts(request):
    if request.method == 'GET':
        #pokemon_facts = pokemon_facts.objects.all()
        return render(request, 'meuapp/index.html', {'API_KEY': API_KEY})  
    
def criar_pokemon_fact(request):
    if request.method == 'POST':
        pokemon_fact = request.POST.get('pokemon_fact')
        pokemon_facts.objects.create(pokemon_fact=pokemon_fact)
        return HttpResponse("Fato de Pokémon criado com sucesso!")
    return render(request, 'meuapp/criar_pokemon_fact.html')

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Pessoa criada com sucesso!")
    else:
        form = PessoaForm()
    return render(request, 'meuapp/criar_pessoa.html', {'form': form})