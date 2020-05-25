""" 
Faça um algoritmo para calcular e escrever o fatorial
de um determinado número lido.
"""

n = int(input())
novo_n = n
j = 1

if n <= 1:
    print(f"Fatorial de {n} vale 1")
else:
    for i in range(n-1):
        f = novo_n * (n-j)
        j += 1
        novo_n = f
    print(f"{n}! = {f}")