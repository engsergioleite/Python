"""
Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez 
a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e 
armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas 
listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
{'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade 
biológica. Dica: use as funções built-in sum() e len().
"""

dicionario = {'Área Norte': [2819, 7236],
              'Área Leste': [1440, 9492],
              'Área Sul': [5969, 7496],
              'Área Oeste': [14446, 49688],
              'Área Centro': [22558, 45148]
              }

dicionarioMedia = {}

for regiao, dados in dicionario.items():
    dicionarioMedia[regiao] = (sum(dados) / len(dados))

for regiao, dados in dicionarioMedia.items():
    mediaMax = regiao, dados

print(f"O dicionário com as médias é: {dicionarioMedia}")

print(f"A região com a maior média é a: {mediaMax}")