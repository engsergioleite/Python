"""
As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 
10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a 
verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada 
para você uma lista com os salários que receberão o abono: 
[1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. 
O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários 
em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o 
abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.
"""

salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = []
dicSalAbono = {}
qtdAbonoMinimo = 0 
custoAbonos = 0
valorMaximo = 0

for i in range(0, len(salarios)):
    abono = (salarios[i] * 10) / 100
    if abono < 200:
        abono = 200
        qtdAbonoMinimo += 1
    abonos.append(abono)

for i in range (0, len(salarios)):
    dicSalAbono[salarios[i]] = abonos[i]

custoAbonos = sum(abonos)
valorMaximo = max(abonos)

print(f"O dicionario de Salário e abonos é o seguinte: {dicSalAbono}")
print(f"O total gasto com abonos foi R${custoAbonos}")
print(f"Um total de {qtdAbonoMinimo} receberam o abono minimo.")
print(f"O valor máximo recebido foi R${valorMaximo}")