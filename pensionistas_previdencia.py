"""Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um 
programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em 
intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo."""



print("CADASTRO DE IDADES")
print("Para interromper, digite um número negativo")
print("")

idade = 0
intervalo1 = 0 # 0-25
intervalo2 = 0 # 26-50
intervalo3 = 0 # 51-75
intervalo4 = 0 # 76-100

while idade >= 0:
    idade = int(input("Escrve a sua idade: "))
    if (idade >= 0) and (idade <= 25):
        intervalo1 += 1
    elif (idade >=26) and (idade <=50):
        intervalo2 += 1
    elif (idade >=51) and (idade <=75):
        intervalo3 += 1
    elif (idade >=76) and (idade <=100):
        intervalo4 += 1

print(f"Tivemos {intervalo1} entre [0-25], {intervalo2} entre [26-50], {intervalo3} entre [51-75] e {intervalo4} entre [76-100]")



