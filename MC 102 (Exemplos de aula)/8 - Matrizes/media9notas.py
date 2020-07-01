""" 
Escreva um programa que leia as notas de 10 exercícios 
de um estudante e calcule a média dos 9 exercícios com 
maiores notas.
"""

NUMERO_EXERCICIOS = 10

def ler_lista_notas(j):
    lista_notas = []
    for _ in range(j):
        nota = float(input())
        lista_notas.append(nota)
    return lista_notas

def obter_indice_menor(lista):
    """Devolve o índice da menor nota"""
    menor_nota = lista[0]
    indice_menor = 0
    for i, nota in enumerate(lista):
        if nota < menor_nota:
            menor_nota = nota
            indice_menor = i
    return indice_menor


def calcular_media_excluida(lista, indice_menor):
    """Devolve a média das notas, excluindo-se a nota de 
    indice indice_menor"""
    soma = 0.0
    for i, nota in enumerate(lista):
        if i != indice_menor:
            soma += nota
    media = soma / (len(lista) -1)
    return media


def main():
    print('Digite as notas dos ecercícios: ')
    lista_notas = ler_lista_notas(NUMERO_EXERCICIOS)
    indice_menor = obter_indice_menor(lista_notas)
    media = calcular_media_excluida(lista_notas, indice_menor)
    print(media) 

main()
