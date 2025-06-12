print("QUAL O TIPO DO TRIANGULO")
print("")
lado1 = float(input("Digite o 1º lado do triangulo: "))
lado2 = float(input("Digite o 2º lado do triangulo: "))
lado3 = float(input("Digite o 3º lado do triangulo: "))
print("")

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2):
    print("A soma de a qualquer dois lados foi maior que o teceiro lado, é um triangulo")
    if (lado1 == lado2 == lado3):
        print("Triangulo Equilatero")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("Triangulo Isósceles")
    elif (lado1 != lado2 != lado3):
        print("Triangulo Escaleno")
else: 
    print("A soma de qualquer dois lados não foi maior que o terceiro lado, não é um triangulo")
    

