listas = ["Sérgio Leite", 9.0, 8.0, 9.5, True]

for i in listas:
    print(i)

"""
for i in range(0, len(listas)):
    print(listas[i])
"""
print("lista com o indice 3 atualizado de 9.5 para 7.0")

listas[3] = 7.0

for i in listas:
    print(i)

print("calculando a média de apenas alguns indices")
media = (listas[1] + listas[2] + listas[3])/3
print(media)