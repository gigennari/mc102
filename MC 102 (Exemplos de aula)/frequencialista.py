

def bubble_sort(lista):
    for _ in range(len(lista)-1):
        for i in range (len(lista)-1):
            if lista[i] > lista[i+1]:
                lista [i], lista[i+1] = lista[i+1], lista[i]
    return(lista)

def encontrar_frequencias(lista):
    lista_frequencia = [] 
    for i in range(len(lista)):
        elemento = lista[i]
        frequencia = 0
        for j in range(len(lista)):
            if elemento == lista[j]:
                frequencia += 1
            else:
                pass
        lista_frequencia.append(frequencia)
    return(lista_frequencia)


def main():
    lista = [3, 8, 5, 8, 6, 5, 2, 3, 4, 3]
    lista_ordenada = bubble_sort(lista)
    lista_frequencia = encontrar_frequencias(lista_ordenada)
    
    print(lista_frequencia)

main()