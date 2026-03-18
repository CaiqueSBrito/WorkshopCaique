from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, 'meuapp/index.html')

def __str__(self):
    return self.nome
    
def ver_pokemon(requests, nome_pokemon):

    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon.lower()}"

    response = requests.get(url)
        
    if response.status_code == 200:
        dados_da_api = response.json()
        print(dados_da_api)
        #contexto = { 'nome': dados_da_api['name']}
