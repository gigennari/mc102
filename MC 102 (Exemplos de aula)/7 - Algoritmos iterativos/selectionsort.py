"""

Algoritmo de seleção 

A lista preta é a lista do índice i até o último 


Para cada índice i  do primeiro até o último 
Selecionar menor elemento na lista preta
Trocar com o primeiro elemento da lista preta 
Continuar com a lista restante 


"""

def indice_menor_lista_preta(lista, i):
    indice_menor = i
    for j in range(i, len(lista)):
        if lista[j] < lista[indice_menor]:  #se o menor que eu conheco até o momento for menor do q o elemento j, descobri um menor ainda
            indice_menor = j
    return indice_menor


def selection_sort(lista):
    for i in range(len(lista)-1):
        indice_menor = indice_menor_lista_preta(lista, i)
        aux = lista[i]
        lista[i] = lista[indice_menor]
        lista[indice_menor] = aux
    return lista



def main():
    lista = [25, 36, 2, 3, 1, 16, 10] 
    lista_ordenada  = selection_sort(lista)
    print(lista_ordenada)

main()