"""
Um usuário deseja escolher que tipo de média e 
calculá-a a partir de 3 notas. Faça um algoritmo que leia as notas, 
a opção escolhida pelo usuário e calcule a média.

"""
import math 

def media_aritmetica(a, b, c):
    media = (a + b + c)/3
    return media

def media_ponderada(a, b, c):
    media = ((3 * a + 3 * b + 4 * c) / 10)
    return media 

def media_harmonica(a, b, c):
    media = (3 / (1/a + 1/b + 1/c))
    return media

def media_geometrica(a, b, c):
    media = ((a*b*c) ** (1/3) )
    return media

def main():
    a = float(input('Insira a 1ª nota: '))
    b = float(input('Insira a 2ª nota: '))
    c = float(input('Insira a 3ª nota: '))
    tipo = input('Insira o tipo de média que gostaria de calcular: ')
    if tipo == 'aritmetica':
        media = media_aritmetica(a, b, c)
    elif tipo == 'ponderada':
        media = media_ponderada(a, b, c)
    elif tipo == 'harmonica':
        media = media_harmonica(a, b, c)
    elif tipo == 'geometrica':
        media = media_geometrica(a, b, c)
    print(f'A média é {media}')

main()