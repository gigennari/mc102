"""

Exponenciação:

a^b = a*a*a*a...*a (b vezes)

a é um numero 
b é um num natural (0, 1, 2, ...)

1) a ^ b = 1    se b=0
2) a ^ b = a*a*a*a* ... *a (b vezes)    se b>=1


"""

def potencia(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b-1)


def main():
    a = 2
    b = 2
    print(f"{a} elevado a {b} é {potencia(a,b)} ")

main()