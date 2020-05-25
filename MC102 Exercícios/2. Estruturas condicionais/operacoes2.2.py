"""
Faça um programa que lê dois números do teclado e em seguida um 
caractere que representa uma operação: +, −, ∗, /. 
Seu programa então deve imprimir o resultado da operação.

"""

x = float(input())
y = float(input())
operacao = input()

if operacao == '+':
    print(x + y)
elif operacao == '-':
    print(x-y)
elif operacao == '*':
    print(x * y)
elif operacao == '/':
    print(f'{x / y:.2f}')
else: 
    print('Operação inválida')