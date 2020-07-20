"""
Dada uma lista de elementos, faça um programa que encontre o maior elemento

Entrada: número seprados por espaços 
lista = [1, 159, 174, 15, 64, 89]

Saída: maior número da lista
174

Caso básico: len(lista) == 1

Caso geral: comparar um  item com o seguinte da lista
se o item 1 for menor, exclui ele da lista
se o item 2 for menor, exclui ele da lista

Verifique de novo o caso básico

""""

def maximo(lista):
    """ Encontra o valor máximo de uma lista desordenada recursivamente"""
    pass

def main():
    numeros = input().split()
    print(numeros)

    numero_maximo = maximo(numeros)
    print(maximo)

main()