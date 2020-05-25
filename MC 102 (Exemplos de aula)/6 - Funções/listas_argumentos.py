""" 

Escreva um programa que leia uma lista de notas
e dê um bônus de 20% para todos os alunos.

"""

def ler_lista_notas():
    """pede que o usuário digite uma 
    lista de notas e devolve"""
    n = int(input("Quantos estudantes há? "))
    lista_notas =[]
    for _ in range(n):
        nota = float(input("Digite as notas dos alunos: "))
        lista_notas.append(nota)
    return lista_notas 

def multiplicar_lista_fator(lista, fator):
    """ Altera a lista de forma que cada
    um dos elementos esteja multiplicado 
    pelo fator """
    for i in range (len(lista)):
        lista[i]= lista[i] * fator
    return lista

def impirmir_lista(lista):
    """ Imprime uma lista de numeros na tela"""
    for indice, numero in enumerate(lista):     #o enumerate devolve o indice e o valor de cada elemento da lista 
        print(f"O estudante {indice} tem nota {numero}")


def main():
    #ler lista de notas
    lista_notas = ler_lista_notas() 
    #incrementar notas em 20%
    lista_incrementada = multiplicar_lista_fator(lista_notas, 1.2)
    #imprimir lista de notas 
    impirmir_lista(lista_notas)

main() 