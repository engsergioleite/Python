loja = {'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
        'precos': [2000, 1500, 3500, 4000, 1500]}

for chave, elementos in loja.items():
  print(f'Chave: {chave}\nElementos:')
  #for dado in elementos:
   # print(dado)

"""
O primeiro laço, o mais externo, faz a leitura dos itens dentro do dicionário (chaves e elementos). 
Sabendo que os elementos são listas, podemos acessar os dados das listas com outro laço de repetição 
que está dentro do primeiro laço. O laço mais interno lê os elementos de cada lista por vez e imprime 
os valores dentro deles.

Além disso, podemos realizar operações comuns em listas, como: adicionar, remover ou contar itens na 
lista associada a uma chave do dicionário.
"""