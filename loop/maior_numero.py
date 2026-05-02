# Exercício 01: Descobrir o maior número digitado
maior = 0 
n = int(input())
for i in range(n):
     numero = int(input("Digite um número: "))
     if numero > maior:
        maior = numero
print(f"Maior = {maior}")