# Exercício 2: Lê valores numéricos, evita duplicatas e exibe em ordem crescente

numeros = []
resposta = "s"

while resposta == "s":
    valor = int(input("Digite um valor: "))
    if valor not in numeros:
        numeros.append(valor)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado, não vou adicionar...")
    resposta = (input("Quer continuar? s/n: "))

numeros.sort()
print(f"Você digitou os valores {numeros}")

