"""
Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, 
você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule 
a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas 
ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.)."""

print("ESTUDO DE TEMPERATURA MÉDIA ANUAL")
print("")

listaMes = []
listaMesAcimaMedia = []
mesAcimaDaMedia = []

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] 
for mes in range(0, 12):
    listaMes.append(float(input(f"Digite a temperatura média do mês {mes+1}: ")))
    dicionarioMeses = listaMes

mediaAnual = sum(listaMes) / 12

for i in range(0, 12):
    if listaMes[i] > mediaAnual:
        listaMesAcimaMedia.append(listaMes[i])
        mesAcimaDaMedia.append(meses[i])
        #print(meses[i])
    
print(f"As temperaturas acima da média anual foram: {listaMesAcimaMedia}")
print(f"Referentes aos meses: {mesAcimaDaMedia}")



