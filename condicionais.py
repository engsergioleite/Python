num1 = float(input('Digite a nota 1: '))
num2 = float(input('Digite a nota 2: '))

media = (num1+num2)/2

"""
if media >= 7:
    print(f"A média foi {media} e o aluno foi aprovado")
else:
    print(f"A média foi {media} e o aluno foi reprovado")
"""

if media >= 7.0:
    print(f"A média foi {media} e o aluno foi aprovado")
if 7.0 > media >= 4.0:
    print(f"A média foi {media} e o aluno esta de recuperação")
if media < 4.0:
    print(f"A média foi {media} e o aluno foi reprovado")