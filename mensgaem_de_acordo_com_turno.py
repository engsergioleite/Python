# Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.


turno = input("Qual turno você estuda [manhã, tarde ou noite] ? ")

if turno == 'manhã':
  print('Bom Dia!')
elif turno == 'tarde':
  print('Boa Tarde!')
elif turno == 'noite':
  print('Boa Noite!')
else:
  print('Valor Inválido!')