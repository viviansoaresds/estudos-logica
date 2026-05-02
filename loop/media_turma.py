# Exercício 02: Calcular média da turma
soma = 0
N = int(input())
for i in range(N):
    notas = int(input("Digite as notas: "))
    soma = soma + notas
media = soma / N
print(f"Media = {media:.2f}")