"""

Escreva um programa que lê três numeros e 
imprime o maior deles

""" 
i = 0
numeros = []

while i<3:
    n = float(input())
    numeros.append(n)
    i += 1

maior = numeros[0]
for i in range(len(numeros)):
    if maior < numeros[i]:
        maior = numeros[i]

print (maior)