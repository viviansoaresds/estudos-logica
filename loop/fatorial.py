# Exercício 04: Descobrir o fatorial de um número

N = int(input())
fatorial = 1
for i in range(1, N + 1):
    fatorial = fatorial * i
print(f"{N}! = {fatorial}")