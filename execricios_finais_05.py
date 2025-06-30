"""Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos 
entre 1 e o número digitado."""


print("CRIAR LISTA DE NUMEROS PRIMOS ENTRE 1 E O NÚMERO DIGITADO")
print("")
numIni = int(1)
numFin = int(input("Digite o número final: "))
lista = []


for numero in range(numIni, numFin): # número vai de 1 até o numero escolhido
    if (numero % 1 == 0) and (numero % numero == 0):
        primo = True
        for testeDivisiveis in range(2, numero):
            if numero % testeDivisiveis == 0:
                primo = False
                break
        if primo == True:
            lista.append(numero)

print(lista)
