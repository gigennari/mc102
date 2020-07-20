"""
Procedimento
se n é par, divida por 2
se n é impar, multiplique por 3, some 1 e divida por 2

A Conjectura de Collaz diz que se repetirmos esse procedimento no resultado da 
execução anterior, chegaremos ao número 1 eventulmente

Entrada: um inteiro positivo
15

Saída: numero de repetições do procedimento para chegar em 1
12

"""

def collatz(contador, n):
     
    if n == 1:
        return contador
    else:
        contador += 1
        if n % 2 == 0:
            n = n / 2
            return collatz(contador, n)
        else:
            n = ((3 * n) + 1) / 2
            return collatz(contador, n)


def main():
    n = int(input())
    
    variavel_contadora = 0
    contador = collatz(variavel_contadora, n)

    print(contador)


main()