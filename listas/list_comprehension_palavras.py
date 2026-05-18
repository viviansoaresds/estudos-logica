# Exercício 1: Filtrando palavras com mais de 4 letras utilizando o List Comprehension

palavras = ["ana", "julia", "vivian", "be", "programacao", "py", "codigoo"]
palavras_longas = [palavra for palavra in palavras if len(palavra) > 4]
print(palavras_longas)