"""
SET 

As operações de listas tbm são válidas para conjuntos 

Vantagens de usar set: 
é mais rápido
não usa busca binária

Desvantagens:
não garante a ordem 
"""


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        lista = []
        for linha in arquivo:
            lista.append(linha.strip())
    return lista

def calcular_diferenca_simetrica(conjunto1, conunto2):
    diferenca = []

    for item in conjunto1:
        if item not in conunto2:  #operação mais rápida do que com lista 
            diferenca.append(item)
    for item in conunto2:
        if item not in conjunto1:
            diferenca.append(item)

    return diferenca

def calcular_diferenca_simetrica_2(A, B):
    diferenca = (A-B).union(B-A)
    return diferenca

def calcular_uniao(A, B):
    uniao = A.union(B)
    return uniao

def calcular_diferenca(A, B):
    diferenca = A - B
    return diferenca

def main():
    A = set(ler_arquivo("a.txt"))   #converte lista em set 
    B = set(ler_arquivo("b.txt"))   #converte lista em set 
    C = calcular_diferenca_simetrica(A, B)
    D = calcular_uniao(A,B)
    E = calcular_diferenca(A, B)
    F = calcular_diferenca_simetrica_2(A, B)
    G = (A & B) #interseção
    H = (A ^ B) #diferença simétrica bem mais simples
    I = (A - B) #letras únicas em A
    J = (A | B) #união dos dois conjuntos

    print(C)    #C e H printam o mesmo conjunto
    print(H)
 

main()