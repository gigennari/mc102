"""
Os jogos feitos na unidade reprsentam alguns problemas:

1) Dada uma lista de valores, encontrar um determinado elemento

2) Dada uma lista de valores ORDENADA, encontrar um determinado 
elemento

BUSCA SEQUENCIAL
-usamos para: procurar palavra em um conjunto;
procurar a posição de inserção no vetor para o algoritmo insertion-sort
- pode ser ineficiente, pois o elementos pode estar na última posição

BUSCA BINÁRIA
-usamos para: procurar valores quando temos uma lista ordenada;
ou então para um conjunto 
-é mais eficiente 

"""

def busca_sequencial(lista, valor_procurado):
    for i, valor in enumerate(lista):
        if valor == valor_procurado:
            return i
    return None #devolve None quando não existe o elemento procurado na lista

def busca_sequencial2(lista, valor_procurado):
    for i, valor in enumerate(lista):
        if valor == valor_procurado:
            return i
    raise ValueError(f"Valor {valor_procurado} não existe na lista")

def encontrar_maximo(n):
    maximo = int(input())
    for _ in range(1, n):
        if numero > maximo:
            maximo = numero
    return maximo