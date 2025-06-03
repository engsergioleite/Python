num1 = input ("digite um número: ")
num2 = input ("digite outro número: ")
terceira_ope = 0

def verificar_resultado(num1, num2):
  terceira_ope = int(num1) * int(num2)
  print(f"Os números escolhidos foram {num1} e {num2}")
  print(f"O resultado da multiplicação entre elas é: {terceira_ope}")
  if terceira_ope >= 10:
    print(f"O resultado foi 10 ou mais e foi igual a: {terceira_ope}")
  elif terceira_ope < 10:
    print(f"O resultado foi menos de 10:{terceira_ope}")
  return terceira_ope
  
terceira_ope = verificar_resultado(num1, num2)

while terceira_ope > 10:
  num1 = input ("digite um número: ")
  num2 = input ("digite outro número: ")
  terceira_ope = verificar_resultado(num1, num2)