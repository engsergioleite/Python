"""Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas 
foram armazenados em um dicionário:

{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

Escreva um código que calcule o total de vendas e o produto mais vendido.
"""

print("ANALISE DE VENDA DE PRODUTOS")
print("")

dadosDeVenda = {'Produto A': 300,
                 'Produto B': 80,
                   'Produto C': 60,
                     'Produto D': 200,
                       'Produto E': 250,
                         'Produto F': 30}
    
soma = sum(dadosDeVenda.values())
# maiorValor = max(dadosDeVenda.values()) # seria o jeito mais prático de fazer, mas fiz usando o for pra exercitar

listaValores = list(dadosDeVenda.values())
maiorValor = listaValores[0]
produtoMaisVendido = ""

for i in range (1, len(listaValores)):
    if listaValores[i] > maiorValor:
        maiorValor = listaValores[i]

# agora vamos achar qual o produto de maior valor

for produto, valor in dadosDeVenda.items():
    if valor == maiorValor:
        produtoMaisVendido = produto
        break

print(soma)
print(maiorValor)
print(produtoMaisVendido)