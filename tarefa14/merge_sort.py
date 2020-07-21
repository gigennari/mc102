"""
Dada uma lista de elementos, o programa devolve a lista em ordem crescente
usando o merge sort 

Entrada: lista de inteiros separados por espaço 
10 2 56 89 31 4 0 23

Saída: str dos numeros em ordem crescente
0 2 4 10 23 31 56 89

Problema:
1) ordenar primeira metade
2) ordenar segunda metade 
3)Intercalar --> percorrer as duas sublistas; inserir o menor valor em uma nova lista;

Caso básico:
incio == fim, sublista contém apenas um elemento, então não há nada a ser feito

Casos gerais:
inicio < fim 
1ª metade
2ª metade

"""

def intercalar(lista, inicio, meio, fim):
    """ Percorre as duas sublistas, intercalando os valores de modo
    que a lista fial seja ordenada crescentemente"""
    pointer1 = inicio
    pointer2 = meio+1
    lista_ordenada = [0 for _ in range(len(lista))]
    
    for i in range(len(lista)):
        if (pointer1 < meio) and (pointer2 < fim):
            if lista[pointer1] < lista[pointer2]:
                lista_ordenada[i] = lista[pointer1]
                pointer1 += 1  
            else:
                lista_ordenada[i] = lista[pointer2]
                pointer2 +=1
        if pointer2 <= fim:
            lista_ordenada[i] = lista[pointer2]
            pointer2 += 1
        elif pointer1 <= meio:
            lista_ordenada[i] = lista[pointer1]
            pointer1 += 1

    return lista_ordenada

def merge_sort(lista, inicio, fim):

    if inicio < fim:
        meio = (inicio + fim) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio+1, fim)
        return intercalar(lista, inicio, meio, fim)
    


def main():
    numeros = input().split()
    for i in range(len(numeros)):
        numeros[i] = int(numeros[i])

    ordenados = merge_sort(numeros, 0, len(numeros)-1)

    print(str(ordenados).strip('[]').replace("'", "").replace(",", "")) 

main()