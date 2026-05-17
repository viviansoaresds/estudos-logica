# Exercício 1: Lê 5 valores, armazena em uma lista e exibe o maior e menor com suas posições

numeros = []
for i in range(5):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    numeros.append(valor)

maior = max(numeros)
menor = min(numeros)

posicao_maior = []
for i in range(len(numeros)):
    if numeros[i] == maior:
        posicao_maior.append(i)

posicao_menor = []
for i in range(len(numeros)):
    if numeros[i] == menor:
        posicao_menor.append(i)

    
print(f"O maior valor digitado foi {maior} nas posições {posicao_maior}")
print(f"O menor valor digitado foi {menor} nas posições {posicao_menor}")

