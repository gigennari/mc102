"""
Considere um programa para determinar se uma sequência de n números
digitados pelo usuário está ordenada ou não. 
Implemente um programa usando uma variável contadora.

"""

#pedir uma sequência de n numeros
#verificar cada item para ver se é menor que todos os outros
#se sim, está ordenada
#se não, não está ordenada 

n = int(input("Quantos números terá sua sequência? "))
i = 0
lista = []

while i < n:
    numero = int(input("Insira o numero: "))
    lista.append(numero)
    i += 1

c = 1
ordenada = True 

for valor in lista:
    for j in range(c, len(lista)):
        if  valor < lista[j]:
            c += 1
            ordenada = True 
        else:
            ordenada = False
            break 

if ordenada == True:
    print('sim')
else:
    print('não')

    
    