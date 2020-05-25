"""
Escreva um porgrama que leia uma lista 
de numeros do teclado e some
a cada um deles um numero 1
"""

def ler_lista_numeros():
    """" Lê uma lista de números de ponto flutuante do teclado e 
    devolve essa lista"""
    lista = []
    n = int(input("Digite quantos elementos: "))
    for _ in range(n):
        numero = float(input())
        lista.append(numero)
    return lista 
    
def incrementar_lista_numeros(lista, n):
    """Altera a lista passada de forma
    a incrementar de 1 cada elemento da lista"""
    nova_lista = []
    for i, valor in enumerate(lista):
        valor += n
        nova_lista.append(valor)
    return nova_lista

def imprimir_lista_numeros(lista):
    """ Imprime lista de numeros recebida 
    na tela, um por linha """
    for valor in lista:
        print(valor)


def main():
    lista_numeros = ler_lista_numeros()
    lista_incrementada = incrementar_lista_numeros(lista_numeros, 1)
    imprimir_lista_numeros(lista_incrementada)

main()