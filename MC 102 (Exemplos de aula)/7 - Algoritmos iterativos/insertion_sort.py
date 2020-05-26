""" 
Insertion sort

Inserir cada elemento em uma nova lista de maneira ordenada

1- lista de itens desordenados 
2- retiramos o primeiro elemento 
3- inserimos este itemem uma nova lista na ordem 
4- repetimos tudo com a lista restante (preta)

Podemos usar uma única lista (um único vetor)
    o primeiro elemeto ja está ordenado
    retirar o primeiro elemento desordenado
    procurar a prosição em que deve ser inserido 
    deslocar os elementos ordenados seguintes
    inserir o elemento retirado na ordem correta 
    continuar com a lista restante 

(i representa o incio da lista preta)

para i do indice i até o último indice:
    chave <-- lista[i]
    j <-- posição de inserção de chave na lista verde (procurar posição em que deve ser inserido)
    descolque os elementos de j até i-1
    lista[j] <-- chave 

"""

def encontrar_posicao(lista, i , chave):
    """
    Devolve a posição de inserção de chave 
    na lista ordenada que vai de 0 até i-1
    """
    seta = 0
    while seta != i and chave > lista[seta]: #para cada indice na lista verde
        seta += 1 
    return seta  #na posição seta, é a primeira posição em que lista[seta] é maior que chave
    
def deslocar_lista(lista, i, j):
    """
    Descolque os elementos de j até i-1 (inclusive)
    Para frente
    """
    k = i
    while k>j:      #vai de trás pra frente 
        lista[k] = lista[k-1]
        k -= 1
    return lista 


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = encontrar_posicao(lista, i, chave)
        deslocar_lista(lista, i, j)
        lista[j] = chave  


def main():
    lista = [2020, 19, 6, 11, 15, 2]
    insertion_sort(lista)
    print(lista)

main()