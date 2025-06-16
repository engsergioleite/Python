print("TRATAMENTO DE DADOS DE AVALIAÇÕES [0 A 5]")
print("")
qtdAva = int(input("Qual a quantidade de avaliações: "))

for i in range(0, qtdAva):
    nota = float(input(f"Digite a {i+1}ª nota entre 0 e 5: "))
       
    while (nota < 0) or (nota > 5):
        nota = float(input(f"Nota inválida, Digite uma nova nota:"))

print("Verificação feita, todas as notas estão válidas.")
        