"""
Busca em um vetor ordenado

Dado um vetor de inteiros em ordem crescente e um número, 
faça um programa busca_binaria.py que retorne o índice da posição 
desse número no vetor ou se esse número não está no vetor.

Entrada: sequência de números separados por espaço e um número i
2 5 6 8 9 16 44 85 
8

Saída: posição de i na sequência ou -1 se não estiver na seq
3
(lembrando que a lista começa na posição 0)

Ideia: verificar lista na posição i

se já percorri todos os números (contador = len(lista)) e lista[contador] != i, devolve -1

caso contrário, 
    se lista [contador] = i, devolvemos contador
    caso contrário,
    contador += 1
    verificar novamente lista[contador]


"""

def busca(lista, contador, num):
    """Acha a posição de um número na lista"""
    if contador == len(lista) and lista[contador] != num:
        return -1
    else:
        if lista[contador] == num:
            return contador
        else:
            contador += 1
            return busca(lista, contador, num)


def main():
    lista = input().split()
    num = int(input())

    for i in range(len(lista)):
        lista[i] = int(lista[i])

    contador = 0
    print(busca(lista, contador, num))

main()