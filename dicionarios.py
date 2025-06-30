cadastro = {"Matricula": 2000168933,
            "Dia do cadastro": 25,
            "Mês_Cadastro": 10,
            "Turma": "2E"}

print(cadastro["Matricula"]) # Acessa a chave e imprime apenas uma chave

cadastro["Matricula"] = "10101010101010" # Acessa a chave e altera o valor

print(cadastro["Matricula"])

cadastro["Modalidade"] = "EAD" # cria uma nova chave e atribui valor


print(cadastro)

# cadastro.pop("Matricula") # Remove a chave Matricula

print(cadastro.items())

print(cadastro.keys())

print(cadastro.values())


for chaves in cadastro.keys():
    print(cadastro[chaves])

for valores in cadastro.values():
    print(valores)

for chaves, valores in cadastro.items(): # A estrutura chaves, valores é devido a items() aplicar essa estrutura
    print(chaves, valores)