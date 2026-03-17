saldo = 0
historico = []

while True:

    print("Banco Fabrica\n 1. Depósito \n 2. Saque \n 3.Extrato \n 4.Sair")
    resposta = int(input("Selecione: "))

    if resposta == 1:
        deposito = (int(input("Quanto você quer depositar:  ")))
        historico.append(f"Você depositou: {deposito}")
        deposito = deposito + saldo

    elif resposta == 2:
        saque = int(input("Quanto você quer sacar: "))
        saldo = saldo - saque
        historico.append(f"Você depositou: {saque}")

    elif resposta == 3: 
        for i in range (len(historico)):
            print(historico[i])

    elif resposta == 4:
        break
