"""
Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
"""

lista = []
for i in range (0,5):
    lista.append(int(input("Digite um número inteiro: ")))
print(lista)

"""Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada."""

lista = []
for i in range (0,5):
    lista.append(int(input("Digite um número inteiro: ")))
lista.sort(reverse=True)

print(lista)

# também posso usar a lógica de partição para imprimir o resultado lista[::-1]
