"""
Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. 
A pesquisa foi feita e o votos computados podem ser observados abaixo:
'''
Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos

Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a 
porcentagem de votos recebidos.
"""

votosMarca = {"Design1": 1334,
              "Design2": 982,
              "Design3": 1751,
              "Design4": 210,
              "Design5": 1811
              }

maiorVotos = max(list(votosMarca.values()))
somaVotos = sum(votosMarca.values())
# for design, votos in votosMarca.items()
designMaisVotado = ""


for design, votos in votosMarca.items():
    if votos == maiorVotos:
        designMaisVotado = design
        break

mediaVotosVencedor = ((maiorVotos * 100) / somaVotos)

print(f"O design mais votado foi o {designMaisVotado} com {maiorVotos} votos e representando {mediaVotosVencedor:.2f}% dos totais de votos.")

