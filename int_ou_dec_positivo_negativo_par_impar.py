# par ou ímpar, positivo ou negativo e inteiro ou decimal.

num1 = float(input("Digite o primeiro número"))
num2 = float(input("Digite o segundo número"))

operacao = input("Qual operação você deseja realizar [+, -, * ou /] ? ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print("Operador não identificado")

print(resultado)

if resultado % 1 == 0:
    print("é um numero inteiro")
else:
    print("é um numero decimal")

if resultado % 2 == 0:
    print("é um numero par")
else:
    print("é um numero impar")

if resultado < 0:
    print("é um numero negativo")
elif resultado == 0:
    print("é um número neutro")
else:
    print("é um numero positivo")