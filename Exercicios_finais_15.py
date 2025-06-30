"""
O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores 
da empresa. Para isso, foram fornecidos os seguintes dados:

{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada 
setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
"""
listaMedia = []
qtdAcimaMedia = 0 
setorIdade = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
              'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
              'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
              'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

for setor, idade in setorIdade.items():
    print(f"A média do {setor} é igual a {sum(idade) / len(idade)} anos.")
    listaMedia.append(sum(idade) / len(idade))

media = sum(listaMedia) / len(listaMedia)

for setor, idade in setorIdade.items():
    for i in range(0, len(idade)):
        if idade[i] > media:
            qtdAcimaMedia += 1

print(f"A média de idade de todos os setores é: {media:.1f}")
print(f"{qtdAcimaMedia} pessoas estão com a idade acima da média")


