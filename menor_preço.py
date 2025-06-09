print("TABELA DE PREÇO DE VEÍCULO")
print("")
preco1 = float(input("Qual o valor do produto 1: "))
preco2 = float(input("Qual o valor do produto 2: "))
preco3 = float(input("Qual o valor do produto 3: "))

menorPreco = preco1

if preco2 < menorPreco:
    menorPreco = preco2
if preco3 < menorPreco:
    menorPreco = preco3

print (f"o carro de menor preço custa R${menorPreco}")

