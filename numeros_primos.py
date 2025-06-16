""" Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, 
por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um 
programa que peça um número inteiro e determine se ele é ou não um número primo."""


num = int(input("Escolha um número para determinar se ele é primo ou não: "))

primo = True

if num <= 1: # números abaixo de 2 não podem ser primos
    primo = False
else:
    for i in range (2, num):
        if num % i == 0:
            primo = False
            break

if primo:
    print(f"o número {num} é primo")
else:
    print(f"o número {num} não é primo")


