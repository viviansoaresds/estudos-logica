# Exercícios de List Comprehension

# Exercício 1: Filtrando palavras com mais de 4 letras

palavras = ["ana", "julia", "vivian", "be", "programacao", "py", "codigoo"]
palavras_longas = [palavra for palavra in palavras if len(palavra) > 4]
print(palavras_longas)

# Exercício 2: Quadrado dos números ímpares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = [ x ** 2 for x in numeros if x % 2 != 0]
print(quadrado)