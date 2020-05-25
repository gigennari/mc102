""" Caclula os valores máximos de duas listas
e devolve o produto e soma entre eles
"""


def ler_lista_numeros():
    n = int(input())
    lista = []
    for _ in range(n):
        numero = int(input())
        lista.append(numero)
    return lista

def obter_maximo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return(maximo)

def obter_produto_soma_maximos(lista1, lista2):
    maximo1 = obter_maximo(lista1)
    maximo2 = obter_maximo(lista2)
    produto = maximo1 * maximo2
    soma = maximo1 + maximo2
    return produto, soma



def main():
    print("Digite uma lista de numeros")
    lista1 = ler_lista_numeros()
    print("Digite uma lista de numeros")
    lista2 = ler_lista_numeros()
    produto, soma = obter_produto_soma_maximos(lista1, lista2) #se não separar por virgula, a variavel devolve uma tupla
    x = obter_produto_soma_maximos(lista1, lista2)
    print(produto)
    print(soma)
    print(x)  #devolve uma tupla

main()

