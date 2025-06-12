print("CALCULADORA DE DESCONTOS DE COMBUSTIVEIS")
tipoCombu = input("Qual o tipo de combustivel você deseja [etanol ou diesel]: ")
qtdCombu = float(input("Digite a quantidade de litros: "))
precoEtanol = float(1.70)
precoDiesel = float(2.00)

if tipoCombu == "etanol":
    if qtdCombu <= 15:
        precoEtanol = precoEtanol - (precoEtanol * 2 /100)
        valorTotal = qtdCombu * precoEtanol
        print(f"O valor a ser pago pelo cliente é: {valorTotal} ")
    else:
        precoEtanol = precoEtanol - (precoEtanol * 4 /100)
        valorTotal = qtdCombu * precoEtanol
        print(f"O valor a ser pago pelo cliente é: {valorTotal} ")

elif tipoCombu == "diesel":
    if qtdCombu <= 15:
        precoDiesel = precoDiesel - (precoDiesel * 3 / 100)
        valorTotal = qtdCombu * precoDiesel
        print(f"O valor a ser pago pelo cliente é: {valorTotal} ")
    else:
        precoDiesel = precoDiesel - (precoDiesel * 5 / 100)
        valorTotal = qtdCombu * precoDiesel
        print(f"O valor a ser pago pelo cliente é: {valorTotal}")
else:
    print("Tipo de combustivel não encontrado.")
