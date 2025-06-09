
# le o valor medio e exibe o mais baixo e mais alto em 3 anos
# opção 1
medAno1 = 6000
medAno2 = 3500
medAno3 = 4000

if medAno2 < medAno1 > medAno3:
    print(f"o maior valor foi o {medAno1}")
elif medAno1 < medAno2 > medAno3:
    print(f"o maior valor foi o {medAno2}")
else:
    print(f"o maior valor foi o {medAno3}")

if medAno2 > medAno1 < medAno3:
    print(f"o menor valor foi o {medAno1}")
elif medAno1 > medAno2 < medAno3:
    print(f"o menor valor foi o {medAno2}")
else:
    print(f"o menor valor foi o {medAno3}")


# opção 2

medAno1 = 8000
medAno2 = 6000
medAno3 = 4000

# determina um maior aleatório

maior = medAno1

if medAno2 > maior:
    maior = medAno2
if medAno3 > maior:
    maior = medAno3

menor = medAno1

if medAno2 < menor:
    menor = medAno2
if medAno3 < menor:
    menor = medAno3

print(f"a média maior foi {maior}")
print(f"a média maior foi {menor}")

