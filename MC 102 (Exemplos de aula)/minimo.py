def encontrar_minimo(lista):
    """Econtra o menor numero em uma lista"""
    if len(lista) == 1:
        return lista[0]
    else:
        minimo = lista[0]
        minimoatual = encontrar_minimo(lista[1:])
        if minimoatual < minimo:
            minimo = minimoatual
        return minimo


def main():
    lista = input().split()
    for i in range(len(lista)):
        lista[i] = int(lista[i])

    print(encontrar_minimo(lista))

main()