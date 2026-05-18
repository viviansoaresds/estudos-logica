# Exercício 2: Quadrado dos números ímpares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = [ x ** 2 for x in numeros if x % 2 != 0]
print(quadrado)