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

def intercalar(esquerda, direita):
    if not len(esquerda):   #se a lista estiver vazia
        return esquerda
    if not len(direita):
        return direita

    resultado = []
    i, j = 0, 0
    while (len(resultado) < len(esquerda) + len(direita)):  #repetir até intercalar todos 
        if esquerda[i] < direita[j]:    #se o elemento da lista da esquerda for menor
            resultado.append(esquerda[i])   #colocar ele na lista resultados
            i+= 1   #aumentar contador da lista da esquerda
        else:   #mesma coisa para a lista da direita
            resultado.append(direita[j])
            j+= 1

        if i == len(esquerda) or j == len(direita): #se, durante o loop, uma lista chegar ao fim, add o restante da outra e encerrar
            resultado.extend(esquerda[i:] or direita[j:])
            break 
    return resultado

def merge_sort(lista):

    if len(lista) < 2:
	    return lista
    else:
        meio = int(len(lista)/2)
        esquerda = merge_sort(lista[:meio])
        direita = merge_sort(lista[meio:])
        return intercalar(esquerda, direita)

def main():
    numeros = input().split()

    for i in range(len(numeros)):
        numeros[i] = int(numeros[i])

    ordenados = merge_sort(numeros)

    print(str(ordenados).strip('[]').replace("'", "").replace(",", "")) 

main()