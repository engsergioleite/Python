raca_caes = ['Labrador Retriever',
             'Bulldog Francês',
             'Pastor Alemão',
             'Poodle']

raca_caes2 = sorted(raca_caes, reverse= True)

print(raca_caes)

# raca_caes.insert(0, "SRD")
raca_caes.insert(len(raca_caes), "SRD") 
# usando o metodo len() o indice indicado será o numero total de elementos da lista, portanto, sera adicionado por ultimo
print(raca_caes)

raca_caes.pop(2)

print(raca_caes)

print(raca_caes.index("SRD"))

print(raca_caes2)

