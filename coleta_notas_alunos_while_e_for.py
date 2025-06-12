"""
cont = 1
while (cont < 5):
    nota1 = float(input("Digite a nota do 1ª bimestre: "))
    nota2 = float(input("Digite a nota do 2ª bimestre: "))
    media = (nota1 + nota2)/2
    print(f"Média igual a: {media}")
    cont += 1
    print(cont)
"""

# Usando o for
for contador in range(1, 6, 1):
    nota1 = float(input("Digite a nota do 1ª bimestre: "))
    nota2 = float(input("Digite a nota do 2ª bimestre: "))
    media = (nota1 + nota2)/2
    print(f"Média igual a: {media}")