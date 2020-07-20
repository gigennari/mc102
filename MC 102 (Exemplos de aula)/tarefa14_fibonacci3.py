"""
Escreve um programa que calcule um Fibonacci modificado

ORIGINAL: 
0,1,1,2,3,5,8,13,21,34,55...

Começa com 0 e 1

fib(0) =0
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3

Sempre soma os dois últimos números para obter o próximo

MODIFICADO: 

f(n) = n                            para 0 =< n =< 2

f(n) = f(n-1) + f(n-2) + f(n-3)     para n > 2

Entrada: um inteiro não negativo
31

Saída: o n-ésimo número da sequencia de fibonacci modificado
83047505
"""

def fib(n):
    """ Calcula o fibonacci modificado de um inteiro n"""
    if n >= 0 and n <=2:
        return n
    else:
        return fib(n-1) + fib(n-2) + fib(n-3)


def main():
    n = int(input())

    print(fib(n))

main()
