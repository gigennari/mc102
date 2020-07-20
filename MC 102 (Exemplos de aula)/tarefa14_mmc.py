"""
O mmc entre dois números a e b é o menor número c que é divisível por a e b.

Entrada: dois inteiros a e b separados por espaço 
12 e 9
Saída: o mmc de a e b
36

12 e 9 --> mdc = 3 --> mmc = 36 --> 12*9 / 3 = 36
12 e 6 --> mdc = 6 --> mmc = 12 --> 12*6 / 6 = 12
15 e 5 --> mdc = 5 --> mmc = 15 --> 15*5 / 5 = 15
21 e 18 --> mdc = 3 --> mmc = 126 --> 21*18 / 3 = 126

Note que o mmc é o produto de a e b, divido pelo mdc 

"""

def mdc(a, b):
    """ Encontra o maior divisor comum entre dois números recursivamente"""
    if a == b:
        return a
    elif a > b:
        return mdc(a - b, b)
    else:
        return mdc(b - a, a)


def mmc(a, b):
    """ Calcula o mmc entre dois números, chamando a função mdc recursiva"""
    return a*b / mdc(a,b)

def main():
    numeros = input().split()
    a = int(numeros[0])
    b = int(numeros[1])

    print(mmc(a, b))

main()