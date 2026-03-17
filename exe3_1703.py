import requests

resposta = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas')
print("Status da Requisição: ", resposta.status_code)
print("Resposta da API: ", resposta.json())