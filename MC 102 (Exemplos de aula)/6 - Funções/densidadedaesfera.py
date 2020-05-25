""" 
Pedir o raio e o peso de uma esfera e
devolver sua densidade
"""

PI = 3.1415

def ler_entrada(entrada):
    """ Lê um número que indica o raio ou peso da esfera """
    dado = float(input(f"Insira {entrada}: "))
    return dado 

def calcular_volume_esfera(r):
    """ Calcula o volume de qualquer esfera"""
    volume = 4/3 * PI * (r ** 3)
    return volume 


def main():
    raio = ler_entrada("o raio da esfera")       #ler raio da esfera
    peso = ler_entrada("o peso da esfera")        #ler peso da esfera
    volume = calcular_volume_esfera(raio)        #calcular volume da esfera
    densidade = peso/volume                     #calcular densidade da esfera 
    print(f"A densidade da esfera é {densidade:.2f}")

main()