# Letra vogao ou consoante
letra = input("Escreva uma letra: ").lower()
vogais = "aeiou"
if letra in vogais: 
    print("Vogal")
else:
    print("Consoante")