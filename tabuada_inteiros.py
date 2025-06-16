"""Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa 
usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:"""


print("TABUADA DE NÚMERO INTEIRO ESCOLHIDO")
print("")
num = int(input("Escolha o número que você quer ver a tabuada: "))

for fator in range(1, 11):
   calc = num*fator
   print(f"{num} * {fator} = {calc}")

