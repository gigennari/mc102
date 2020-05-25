"""
Algoritmo da bolha 

Dada uma lista,

#Coloquei o ultimo no lugar 
Para cada índice i do primeiro ao penúltimo, 
Compare cada elemento i com o i+1
Se tiverem fora de ordem, troque 

#Coloquei o penúltimo no lugar 
Para cada índice i do primeiro ao penúltimo, 
Compare cada elemento i com o i+1
Se tiverem fora de ordem, troque 
...

Ou seja, no repita n-1 vezes

"""
def bubble_sort(lista):
    for _ in range(len(lista)-1):
        for i in range (len(lista)-1):
            if lista[i] > lista[i+1]:
                lista [i], lista[i+1] = lista[i+1], lista[i]
    return(lista)


def main():
    lista = input().split()
    lista = bubble_sort(lista)
    print(lista)

main()