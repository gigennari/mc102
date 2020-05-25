"""Escreva um programa que desenha um disco na tela
usando caracteres 

""" 


def ler_raio():
    r = int(input("Digite o raio do disco: "))
    return r

def desenhar_disco(raio):
    for i in range(-raio, raio+1):
        for j in range(-raio, raio+1):
            if i ** 2 + j ** 2 <= raio ** 2:        #verifica se o ponto está contido no disco
                print("*", end="")
            else:
                print(" ", end="")
        print()     #imprime quebra de linha 


def main():
    raio = ler_raio()
    desenhar_disco(raio)

main()