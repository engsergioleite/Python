conjuntoPares = {2, 4, 6, 8}
conjuntoImpares = {1, 3, 5, 7}
conjuntoTodos = {1, 2, 3, 4}

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in conjuntoImpares:
    print(i)

setLista = set(lista)

print(len(setLista))

print(set.isdisjoint(conjuntoPares, conjuntoImpares))


print(set.intersection(conjuntoPares, conjuntoTodos))

print(conjuntoPares & conjuntoTodos)

print(conjuntoTodos | conjuntoPares | conjuntoImpares | set(lista))