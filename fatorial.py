""" Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. 
Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus 
antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120."""

print("CALCULO DE FATORIAL DE UM NÚMERO INTEIRO")
print("")

num = int(input("Escolha um número inteiro para ser transformado em fatorial: "))

fatorial = 1

while num >= 1:
    fatorial *= num
    print(fatorial)
    num -= 1




