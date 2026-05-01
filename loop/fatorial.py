# Exercício 04: Tabuada 

N = int(input())
fatorial = 1
for i in range(1, N + 1):
    fatorial = fatorial * i
print(f"{N}! = {fatorial}")