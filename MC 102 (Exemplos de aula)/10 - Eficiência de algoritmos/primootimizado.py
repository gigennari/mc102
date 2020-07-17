"""
Como otimizar:

-se um num é par maior que 2, não precisamos verificar se é primo
com a função, pois NÃO é

-se um num não tem divisores maior um e menor ou igual 
a sua raiz, ele É primo     #evita checar todos os numeros entre 
a raiz de n e n

SEM MUDANÇAS
n=100       user    0m0,025s
n=10000     user    0m2,713s
n= 100000   user    4m37,849s 
COM MUDANÇAS
n=100       user    0m0,025s
n=10000     user    0m0,049s
n= 100000   user    0m0,495s

Para um algoritmo mais eficiente ainda, poderiamos eliminar a checagem 
de números múltiplos de primos por exemplo (2p, 3p, 4p, 5p...)


n=100       user    0m0,021s 
n=10000     user    0m0,028s    
n= 100000   user    0m0,051s

Ele fica mais rápido ainda!

"""
import math 

def contar_crivo_estatostenes(n):
    """ Cria uma lista de bools em que True representa um num
    que com certeza não é primo, pois é 0, 1 ou múltiplo de um num
    diferente de 1 e ele próprio """
    m=0
    riscados = [False] * n

    riscados[0] = True
    riscados[1] = True
    
    for p in range(n):
        if not riscados[p]: #not riscados --> tem que ser falso
            m += 1
            for q in range(2*p, n, p):
                riscados[q] = True
    return m 


def main():
    n = int(input('Digite o número n: '))
    m = contar_crivo_estatostenes(n)
    print(f'Há {m} primos de 0 ate {n-1}')

main()