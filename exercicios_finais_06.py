"""Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para 
uma análise."""

print("ESCREVA UMA DATA PARA ANALISAR SE ELA É VÁLIDA")
print("FORMATO DD/MM/AAAA")
print("")
data = input("Escreva DD/MM/AAAA:")

dataLista = data.split("/")

dataDicionario = {"Dia": int(dataLista[0]), 
                  "Mês": int(dataLista[1]),
                  "Ano": int(dataLista[2])}

if (dataDicionario["Dia"] >= 1) and (dataDicionario["Dia"] <= 31):
    if (dataDicionario["Mês"] >= 1) and (dataDicionario["Dia"] <= 12):
        if (dataDicionario["Ano"] >= 1) and (dataDicionario["Dia"] <= 3000):
            print("Data correta")
else: 
    print("Data incorreta")


