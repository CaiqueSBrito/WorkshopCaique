class Calc:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def somar(self):
        return self.num1 + self.num2

    def subtrair(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 == 0:
            return "Erro: Divisão por zero"
        return self.num1 / self.num2

historico = []

while True:
    print("\nCalculadora \n 1. Soma \n 2. Subtrair \n 3. Multiplicar \n 4. Dividir \n 5. Historico\n 6. Sair")
    escolha = input("Selecione: ")

    if escolha == '6':
        print("Saindo da calculadora")
        break
    
    if escolha == '5':
        print("\n--- Histórico ---")
        for i in range(len(historico)):
            print(historico[i])
        continue
    try:
        n1 = input("1º número: ")
        n2 = input("2º número: ")
        minha_calc = Calc(n1, n2)
        
        if escolha == '1':
            resultado = minha_calc.somar()
            print(f"Resultado: {resultado}")
            historico.append(f"Soma de {n1} + {n2} = {resultado}")
            
        elif escolha == '2':
            resultado = minha_calc.subtrair()
            print(f"Resultado: {resultado}")
            historico.append(f"Subtração de {n1} - {n2} = {resultado}")
            
        elif escolha == '3':
            resultado = minha_calc.multiplicar()
            print(f"Resultado: {resultado}")
            historico.append(f"Multiplicação de {n1} * {n2} = {resultado}")
            
        elif escolha == '4':
            resultado = minha_calc.dividir()
            print(f"Resultado: {resultado}")
            historico.append(f"Divisão de {n1} / {n2} = {resultado}")
        else:
            print("Opção inválida.")

    except ValueError:
        print("Erro: Por favor, digite apenas números.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")