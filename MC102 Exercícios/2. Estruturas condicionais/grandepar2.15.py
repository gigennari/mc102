"""
Considere um problema de decidir se um número inteiro é grande par,
sso é, se ele é par, maior que 100 e vale o dobro de um número ímpar.
 Escreva um programa que leia um número e imprime “SIM” quando for grande par, 
e “NÃO” caso contrário.

"""
#ler numero 

#se par and maior que and dobro de ímpar:
    #imprimir sim 
#imprimir não 

n= int(input())

if n % 2 == 0 and n > 100:
    if (n/2) % 2 == 1:
        print(f"{n} é grande par")
    else:
        print(f"{n} não é grande par")