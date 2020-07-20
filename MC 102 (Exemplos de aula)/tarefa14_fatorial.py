"""
Escreva um porgrama que calcula o fatorial de um número

Ex: 5! = 5*4*3*2*1 = 120

Entrada: número int n não negativo
5

Saída: p fatorial de n
120

Caso básico: 
n! = 1                              se n = 1

Caso geral:
n! = n * (n-1) * (n-2) * ... 1      se n > 1
ou seja, é n * (n-1)!


"""



def fatorial(n):
    """Calcula o fatorial de um número n recursivamente"""
    if n == 0:
        return 1
    else:
        return fatorial(n-1) * n

def main():
    n = int(input())

    print(fatorial(n))