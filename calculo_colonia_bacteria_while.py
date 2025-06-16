
colBacA = 4
colBacB = 10

taxCrescA = 3
taxCrescB = 1.5

dia = 0

while (colBacA < colBacB):
    colBacA = ((colBacA * taxCrescA) / 100) + colBacA
    colBacB = ((colBacB * taxCrescB) / 100) + colBacB
    dia += 1

print(dia)
