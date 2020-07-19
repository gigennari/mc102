"""
Sequencia de fibonacci: 0,1,1,2,3,5,8,13,21,34,55...

Começa com 0 e 1

fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3

Sempre soma os dois últimos números para obter o próximo
"""

def fib(n):
    """ Calcula o fib de um número n recursivamente"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def main():

    for n in range(0,11):
        print(f"fib({n}) = {fib(n)}")

main()