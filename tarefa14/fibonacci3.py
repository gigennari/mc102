"""
Escreve um programa que calcule um Fibonacci modificado

ORIGINAL: 
0,1,1,2,3,5,8,13,21,34,55...

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

O tempo de execução diminui usando um dict para armazenar todos os fib já calculados 
"""

def fib(n, valores_conhecidos):
    """ Calcula o fibonacci modificado de um inteiro n"""
    if n in valores_conhecidos:
        return valores_conhecidos[n]
    else:
        intermediario = fib(n-1, valores_conhecidos) + fib(n-2, valores_conhecidos) + fib(n-3, valores_conhecidos)
        valores_conhecidos[n] = intermediario
        return valores_conhecidos[n]


def main():
    n = int(input())

    valores_conhecidos = {0:0, 1:1, 2:2}
    print(fib(n, valores_conhecidos))

main()
