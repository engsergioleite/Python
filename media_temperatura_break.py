""" Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a
 média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C."""

temp = float(input("Digite a temperatura em °C: "))
contador = 1 
soma = 0

while temp != -273:
    temp = float(input("Digite a temperatura em °C: "))
    soma += temp
    contador += 1
    
media = temp / contador 

print(f"A média entre as {contador} temperaturas registradas foi de {media}.")