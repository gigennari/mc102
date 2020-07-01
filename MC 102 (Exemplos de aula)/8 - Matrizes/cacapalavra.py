"""
Escreva um programa que leia uma palavra e depois leia uma matriz 
de caracteres de dimensões 15 x 20.

A matriz contém, em cada linha, uma linha do caça palavras.

O programa deverá contar o número de vezes que a palavra aparece.

"""

def ler_arquivo_entrada(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        palavra = arquivo.readline().strip()
        matriz = []
        for linha in arquivo:
            matriz.append(linha.strip())
    return palavra, matriz 

def verificar_horizontal(palavra, matriz, i, j):
    """ Devolve True se a palavra ocorre em matriz horizontalmente
    a partir da da coluna j da linha i""" 
    tamanho = len(palavra)
    for k in range(tamanho):
        if j + k >= len(matriz[i]) or palavra[k] != matriz[i][j+k]:
            return False      
    return True

def verificar_vertical(palavra, matriz, i, j):
    tamanho = len(palavra)
    for k in range(tamanho):
        if i + k >= len(matriz) or palavra[k] != matriz[i+k][j]:
            return False  
    return True 

def contar_ocorrencias(palavra, matriz):
    """ 
    para cada linha i:
        para cada coluna j da linha i:
            se a palavra começa na coluna j horizontalmente:
                conte uma ocorrência 
            se a palavra começa na coluna j horizontalmente:
                conte uma ocorrência
    """
    m = len(matriz)
    n = len(matriz[0])
    ocorrencias = 0
    for i in range(m):
        for j in range(n):
            if verificar_horizontal(palavra, matriz, i, j):
                ocorrencias += 1
            if verificar_vertical(palavra, matriz, i, j):
                ocorrencias += 1
    return ocorrencias


def main():
    palavra, matriz = ler_arquivo_entrada("cacapalavras.txt")       #ler arquivo 
    ocorrencias = contar_ocorrencias(palavra, matriz)
    print(f"Há {ocorrencias} ocorrências")

main() 