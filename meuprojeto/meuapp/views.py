from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa, pokemon_facts
from .forms import PessoaForm

def home(request):
    return render(request, 'meuapp/index.html')
# Create your views here.

def listar_usuarios(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'meuapp/listar_usuarios.html', {'pessoas': pessoas})

def listar_pokemon_facts(request):
    if request.method == 'GET':
        pokemon_facts = pokemon_facts.objects.all()
        return render(request, 'meuapp/pokemon_facts.html', {'pokemon_facts': pokemon_facts})  
    
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