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

while True:
    print("\nCalculadora \n 1. Soma \n 2. Subtrair \n 3. Multiplicar \n 4. Dividir \n 5. Sair")
    escolha = input("Selecione: ")

    if escolha == '5':
        break

    n1 = input("1º número: ")
    n2 = input("2º número: ")
    
    minha_calc = Calc(n1, n2)

    if escolha == '1':
        print(f"Resultado: {minha_calc.somar()}")
    elif escolha == '2':
        print(f"Resultado: {minha_calc.subtrair()}")
    elif escolha == '3':
        print(f"Resultado: {minha_calc.multiplicar()}")
    elif escolha == '4':
        print(f"Resultado: {minha_calc.dividir()}")