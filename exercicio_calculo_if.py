
print("CALCULADORA")
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
operacao = input("Digite qual operador você deseja usar (+, -, * ou /): ")
resultado = 0

if operacao == "+":
    resultado = num1 + num2
if operacao == "-":
    resultado = num1 - num2
if operacao == "*":
    resultado = num1 * num2
if operacao == "/":
    resultado = num1 / num2


print(resultado)