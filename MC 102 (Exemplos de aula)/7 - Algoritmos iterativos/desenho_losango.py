"""
Escreva um programa que desenha um losango na tela
usando caracteres ***

"""


def absoluto(valor):
    if valor < 0:
        return -valor
    else:
        return valor 

def desenhar_losango(diagonal_menor):

    raio = diagonal_menor / 2
      
    for linha in range(1, 2*raio + 1):
        num_espaco = absoluto(raio - linha)
        num_asterisco = 2 * (raio - num_espaco) 
        str_espaco = " " * num_espaco
        str_asterisco = "*" * num_asterisco
        print(str_espaco, end="")
        print(str_asterisco)



def main():
    desenhar_losango(20)


main()