#Desafio 1
print("Olá, mundo!")

#Desafio 2
nome = "Caique"
print(nome)

#Desafio 3
def somar(a, b):
    return a + b

resultado = somar(10, 5)
print(resultado)

#Desafio 4
def dividir(a, b):
    return a / b
while True:
    try:
        numeros = [10, 20, 30]
        indice = int(input("Digite um índice para acessar a lista: ")) 
        leng_indice = len(numeros) - 1
        print(numeros[indice])
        break
    except IndexError:
        print("Index inválido")

#Desafio 5
while True:
    try:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

        resultado = dividir(int(num1), int(num2))
        print(f"Resultado: {resultado}")
        break
    except ValueError:
        print("Valor inválido")
    except ZeroDivisionError:
        print("Divisão por zero")

#Desafio 6
while True:
    try:
        dados = {
            "nome": "Isaac ",
            "idade": 25,
            "cidade": "São Paulo"
        }

        chave = input("Digite a chave que deseja acessar: ")

        print(f"O valor da chave '{chave}' é: {dados[chave]}")
        break
    except KeyError:
        print("Chave inválida")

#Desafio 7
while True:
    try:
        def validar_idade(idade):
            if idade < 0 or idade > 120:
                raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
            return f"Idade válida: {idade}"

        idade = int(input("Digite sua idade: "))
        print(validar_idade(idade))
        break
    except ValueError:
        print("Tipo inválido")