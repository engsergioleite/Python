"""Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais 
e calcule a porcentagem quanto ao total de compras"""

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

contador = 0
soma3000 = 0

for indice in range(0, len(gastos)):
    if gastos[indice] > 3000:
        contador += 1
        soma3000 += gastos[indice]
       

gastoTotal = sum(gastos)


percentual = (soma3000 * 100) / gastoTotal 

print(percentual)

print(f"Foram comprados o total de {contador} carros acima de R$3000.00, representando a soma de R${soma3000} e {percentual: .2f}% em relação ao total que foi de R${gastoTotal}.")
