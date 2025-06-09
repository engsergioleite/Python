# Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

num = int(input("Escreva um número inteiro: "))

calc = (num % 2)

if calc == 0:
    print("Número Par")
else:
    print("Número impar")
