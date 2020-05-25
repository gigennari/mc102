""" Considere uma lista de inteiros não negativos L, possivelmente com repetição
Queremos calcular a probabilidade de um número de ser escolhido quando 
sorteamos um elemento da lista aleatoriamente.

Você deve criar uma lista L' em que cada número de ocorra apenas uma vez. 
Os elementos de devem estar na ordem de menos provável para mais provável.
No caso de dois números diferentes terem a mesma probabilidade,
o menor elemento deve vir antes."""


def bubble_sort(lista):     #trocar dois a dois até ordenar a lista 
    "Ordena a lista incial, avaliando os numeros dois a dois. Essa ordenação no início, evita uma ordenação mais complexa das probabilidades no programa"
    for j in range(len(lista)-1):       #para cada numero na lista do começo para o final
        for i in range (len(lista)-1):      #checar em toda a lista
            if lista[i] > lista[i+1]:       #se o número que vem depois é menor, 
                aux = lista [i]     #se sim, inverter suas posições
                lista[i] = lista[i+1]
                lista[i+1] = aux    
    return(lista)

def encontrar_frequencias(lista):
    lista_frequencia = [] 
    for i in range(len(lista)): 
        elemento = lista[i]     #definir umu elemento inicial
        frequencia = 0
        for j in range(len(lista)):     #verficar quantas vezes o elemnto escolhido se repete na lista
            if elemento == lista[j]:
                frequencia += 1
        lista_frequencia.append(frequencia)     #no fim da checagem para cada numero, adiciona a frequencia na lista de frequencia 
    return lista_frequencia

def eliminar_repeticao(lista1, lista2):
    " Elimina as repetições nas listas ordenadas dos números inseridos e de suas respectivas frequências" 
    lista_sem_rep = []
    freq_sem_rep = []
    for i in range(len(lista1)):
        if lista1[i] not in lista_sem_rep:      #se o elemento i da lista 1 ainda não estiver na lista 
            lista_sem_rep.append(lista1[i])     #adicionar elemento i da lista 1 na lista dos numeros sem repetições
            freq_sem_rep.append(lista2[i])      #adicionar o elemento i da lista 2 na lista das frequencias sem repetições 
    return lista_sem_rep, freq_sem_rep
    
def obter_indice_menor(lista):
    "Obtem o indice do menor numero de uma lista"
    minimo = lista[0]
    posicao = 0
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
            posicao = i
    return(posicao)       

def listar_em_probabilidade_crescente(lista1, lista2):
    " Encontra a menor frequencia em uma lista2 e adiciona a uma lista final o elemento correspondente a essa probabilidade na lista 1. Conforme o mínimo é achado na lista2 de frequência, é necessário eliminar ele e seu número correspondente na lista1."
    lista_crescente = []
    for i in range(len(lista1)):
        indice = obter_indice_menor(lista2)
        lista_crescente.append(lista1[indice])
        lista1.pop(indice)
        lista2.pop(indice)
    return lista_crescente

        
def main():
    lista = input().split(' ')      #receber os valores dessa lista
    lista_ordenada = bubble_sort(lista)     #colocar lista em ordem crescente
    lista_frequencia = encontrar_frequencias(lista_ordenada)        #calcular frequencia (equivalente à prob)
    ordenada_sem_rep, frequencia_sem_rep = eliminar_repeticao(lista_ordenada, lista_frequencia)         #eliminar numeros repetidos 
    lista_final = listar_em_probabilidade_crescente(ordenada_sem_rep, frequencia_sem_rep)
    for valor in lista_final:
        print(valor, end=" ")

main()