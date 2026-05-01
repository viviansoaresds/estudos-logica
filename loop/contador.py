# Exercício 03: Contador de números positivos e negativos

positivo = 0
negativo = 0
N = int(input())
for i in range(N):
    numeros = int(input("Digite um número: "))
    if numeros > 0:
        positivo = positivo + 1
    elif numeros < 0:
        negativo = negativo + 1
print(f"Positivos = {positivo}")
print(f"Negativos = {negativo}")

