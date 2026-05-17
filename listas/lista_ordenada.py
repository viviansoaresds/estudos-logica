# Exercício 3: Lê 5 valores e insere cada um na posição correta sem usar sort
numeros = []
for i in range(5):
    valor = int(input("Digite um valor: "))
    
    for posicao in range(len(numeros)):
        if numeros[posicao] > valor:
            numeros.insert(posicao, valor)
            print(f"Adicionado na posição {posicao} da lista...")
            break
    else:
        numeros.append(valor)
        print(f"Adicionado ao final da lista...")
print(f"Os valores digitados em ordem foram {numeros}")