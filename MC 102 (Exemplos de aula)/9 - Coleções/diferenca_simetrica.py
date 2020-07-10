"""
Escreva um programa que,
dadas duas listas de números inteiros,
devolva a diferença simétrica da lista 

A = {1, 2, 5, 7}
B = {2, 5, 8, 10}

A U B = {1, 2, 5, 7, 8, 10}
A intersec B = {2, 5}
A \ B = {7, 1}  # A - B é quem está em A e não está em B 

dif simétrica  = #quem ta em A e não tá em B OU quem tá em B e não tá em A

A dif B = {1, 7, 8, 10} 
podemos achar esse conjunto fazendo a uniao - a interseção 

"""

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        lista = []
        for linha in arquivo:
            lista.append(linha.strip())
    return lista

def calcular_diferenca_simetrica(lista1, lista2):
    diferenca = []

    for item in lista1:
        if item not in lista2:  #percorrer a lista 2 inteira torna o algoritmo lento
            diferenca.append(item)
    for item in lista2:
        if item not in lista1:
            diferenca.append(item)

    return diferenca


def main():
    A = ler_arquivo("a.txt")
    B = ler_arquivo("b.txt")
    C = calcular_diferenca_simetrica(A, B)
    print(C)

main()