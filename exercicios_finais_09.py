"""
Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve 
pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual 
ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B
"""

gabarito = {1: "D",
            2: "A",
            3: "C",
            4: "B",
            5: "A",
            6: "D",
            7: "C",
            8: "C",
            9: "A",
            10: "B"
            }

print("CONFERÊNCIA DE GABARITO - 10 QUESTÕES")
print("")
notas = {}
pontos = 0
for i in range(0, 10):
    letra = input(f"Informe a resposta da {i+1}ª questão: ")
    notas[i+1] = letra # acessando o dicionário e cadastrando uma nota na posição so indice + 1

print("GABARITO")
print(gabarito)
print("NOTAS")
print(notas)

for i in range(0, 10):
    if gabarito[i+1] == notas[i+1]:
        pontos += 1

print(f"O aluno acertou {pontos} questões.")

    

