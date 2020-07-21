"""
Dados dois números inteiros e positivos a e b,
calculamos a^b fazendo, no máximo, log2(b) + 1 chamadas recursivas

Entrada: dois inteiros positivos separados por espaço
2 3

Saída: a^b
8

Problema:
Fazer, no máximo, log2(b)+1 chamadas significa fazer uma chamada para b diminuindo
de 1 em 1 e definir o caso básico como um número elevado a 1 é ele mesmo

"""

def potencia(a, b):
    """ Calcula potencias recursivamente """
    if b == 1:
        return a    #a elevado a 1 é o próprio a 
    else:
        return a * potencia(a, b-1)


def main():
    a, b = input().split()
    a = int(a)
    b = int(b)

    print(potencia(a, b))


main()