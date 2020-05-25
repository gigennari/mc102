"""
Escreva um porgrama que leia uma lista 
de numeros do teclado e some
a cada um deles um numero 5
"""
import util_listas

def main():
    lista_numeros = util_listas.ler_lista_numeros()
    lista_incrementada = util_listas.incrementar_lista_numeros(lista_numeros, 5)
    util_listas.imprimir_lista_numeros(lista_incrementada)

main()