"""Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). 
Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados 
pelo número 6).
Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os 
votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos 
e a porcentagem de votos em branco em relação ao total de votos."""

cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
nulo5 = 0
branco6 = 0 

for eleitor in range(1, 21):
    print("")
    print("ELEIÇÃO PARA GERÊNCIA DA EMPRESA")
    print("")
    print("[1] - Candidato 1")
    print("[2] - Candidato 2")
    print("[3] - Candidato 3")
    print("[4] - Candidato 4")
    print("[5] - Nulo")
    print("[6] - Branco")
    print("")
    voto = int(input(f"Qual o seu voto, colaborador {eleitor}: "))
    if (voto < 1) or (voto > 6):
        print("Voto errado!")
    elif voto == 1:
        cand1 += 1
    elif voto ==2:
        cand2 +=1
    elif voto ==3:
        cand3 +=1
    elif voto ==4:
        cand4 +=1
    elif voto ==5:
        nulo5 +=1
    elif voto ==6:
        branco6 +=1
    
porcentualNulo = nulo5 * 100 / (cand1 + cand2 + cand3 + cand4 + nulo5 + branco6)
porcentualBranco = branco6 * 100 / (cand1 + cand2 + cand3 + cand4 + nulo5 + branco6)

print(f"O Candidato 1 recebeu {cand1} votos.")
print(f"O Candidato 2 recebeu {cand2} votos.")
print(f"O Candidato 3 recebeu {cand3} votos.")
print(f"O Candidato 4 recebeu {cand4} votos.")
print(f"O Nulo recebeu {nulo5} votos.")
print(f"O Branco recebeu {branco6} votos.")


print(f"O percentual de votos Nulos em relação a todos os votos foi de {porcentualNulo}%")
print(f"O percentual de votos em branco em relação a todos os votos foi de {porcentualBranco}%")

# poderia ter feito o calculo direto no print, sem ter que declarar variavel antes.
"""
print(f'Percentual de votos nulos: {(votos_nulos / 20 * 100)}')
print(f'Percentual de votos em branco: {(votos_branco / 20 * 100)}')
"""
    

