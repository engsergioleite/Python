"""Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número 
de bactérias por dia (em milhares) e pode ser observado a seguir: 
[1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma 
lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada 
dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a 
seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada)."""

numBac = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9] # Número de bacterias em milhões
listaPercentual = []

for elemento in range(1, len(numBac)):
    # crescimentoPercentDia = ((numBac[elemento] * 100) / numBac[elemento-1]) - 100
    crescimentoPercentDia = 100 * (numBac[elemento] - numBac[elemento-1]) / numBac[elemento-1]
    crescimentoPercentDiaArredondado = round(crescimentoPercentDia, 2)
    listaPercentual.append(crescimentoPercentDiaArredondado)        

print(listaPercentual)


 

