""" 
Escreva um programa que lê um número inteiro do teclado e 
imprime "sim" se o número for par e maior do que 10, ou for ímpar 
e menor do que 50. 
Caso contrário o programa deve imprimir "não".

"""
n = int(input())

if (n % 2 == 0 and n>10) or (n % 2 == 1 and n<50):
    print('Sim')
else:
    print('Não')
