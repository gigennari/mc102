def obter_maximo(lista):
    assert len(lista) > 0, "Lista deve ter pelo menos um elemento"
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return(maximo)

def main():
    lista = []
    lido = int(input())
    while lido != 0:
        lista.append(lido)
        lido = int(input())
    print(lista)
    print(obter_maximo(lista))

main()