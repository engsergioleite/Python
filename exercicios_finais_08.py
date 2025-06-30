"""Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números 
inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que 
colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos."""

print("COLETA DE 10 IDs E SEPARAÇÃO POR NÚMEROS INTEIROS PAR OU IMPAR")
print("")

listaPar = []
listaImpar = []
qtdPar = 0
qtdImpar = 0

for i in range(0,10):
    numId = float(input(f"Digite o {i+1}º número inteiro: "))
    if (numId % 1) == 0:
        if (numId % 2) == 0:
            listaPar.append(numId) #par
            qtdPar += 1
        else:
            listaImpar.append(numId) #impar
            qtdImpar += 1
    else:
        print("não é número inteiro, digite outro número")

print(f"Tivemos {qtdPar} números par que são DOCES e armazenados na lista {listaPar}")    
print(f"Tivemos {qtdImpar} números impar que são AMARGOS armazenados na lista {listaImpar}")
