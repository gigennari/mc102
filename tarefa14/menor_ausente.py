"""
Dada uma seuquência ordenada (crescente) de números, o programa encontra 
o menor elemento ausente dessa sequência 

Entrada: uma sequência ordenada de números separados por espaço 
0 1 2 3 4 5 6 7 8 9 10 11 13 14 15 16

Saída: o menor número ausente da seuência 
12

Caso básico:
numero atual é diferente do numero esperado, sendo numero esperado
o elemento anterior da lista mais 1

Caso geral:

incrementar 1 na posição a ser verificada
atualizar numero esperado para a proxima recursao
chamar a função novamente 

"""

def menor_ausente(lista, posicao, numeroesperado):
    """Acha o menor numero ausente em uma lista ordenada"""
    if lista[posicao] != numeroesperado:
        return posicao
    else:
        posicao += 1
        numeroesperado += 1
        return menor_ausente(lista, posicao, numeroesperado)


def main():
    lista = input().split()
    for i in range(len(lista)):
        lista[i] = int(lista[i])


    print(menor_ausente(lista, 0, lista[0]))

main() 