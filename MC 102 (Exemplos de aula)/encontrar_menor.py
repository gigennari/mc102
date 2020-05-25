


def obter_maximo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return(maximo)

def obter_minimo(lista):
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return(lista[minimo])

def main():
    lista  = [2, 3, 3, 3, 4, 5, 5, 6, 8, 8]
    lista_frequencia = [6, 3, 3, 1, 1, 2, 2, 1, 2, 2]
    minimo = obter_minimo(lista_frequencia)
    print(minimo)

main()
