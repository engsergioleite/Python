num1 = int(input("Escreva o 1º número inteiro: "))
num2 = int(input("Escreva o 2º número inteiro: "))
num3 = int(input("Escreva o 3º número inteiro: "))


# encontrar o maior e menor

if (num1 >= num2) and (num1 >= num3):
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
    
elif (num2 >= num1) and (num2 >= num3):
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
else:
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)
        
    



