print("IMPRIME NÚMEROS INTEIROS ENTRE NÚMEROS")
num1 = int(input("Digite o 1º número inteiro: "))
num2 = int(input("Digite o 2º número inteiro: "))

#contador = 0

if num1 < num2 or num1 < num2:
    for contador in range (num1, num2): # se é de 1 em 1 nao precisa do passo
        if (contador > num1) and (contador < num2):
            print(contador)
else:
    print("números iguais")