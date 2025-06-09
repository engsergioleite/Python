# Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

num = float(input("Escreva um número: "))


"""
if "." in num:
    print("número decimal")
else:
    print("número inteiro")
"""

if num % 1 == 0:
    print("número inteiro")
else:
    print("número decimal")