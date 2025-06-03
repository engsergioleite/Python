nome_aluno = 'Fabricio Daniel'


nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

# usando o método f-string

print(f"o nome do aluno é: {nome_aluno}, ele tem a idade de {idade_aluno} e média {media_aluno}")

# usando o método de operador %
print('Nome do aluno: %s' %(nome_aluno))
print('Nome do aluno é %s, ele tem %d anos e sua média é %f.' %(nome_aluno, idade_aluno, media_aluno))

# usando o método format()

print("O nome do aluno é: {}".format(nome_aluno))
print("O nome do aluno é {}, ele tem idade \n {} e media {}".format(nome_aluno, idade_aluno, media_aluno))