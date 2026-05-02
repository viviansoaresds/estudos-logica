# Exercício 02: Verificar se a pessoa tem idade para dirigir

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode tirar carteira de motorista.")
elif idade >= 16:
    print("Você ainda não tem idade para dirigir, mas está perto.")
else:
    print("Você não pode dirigir!")