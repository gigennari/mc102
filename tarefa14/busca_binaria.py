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

Isso é busca sequencial 
Busca binária divide lista na metade 

Caso básico: só há 1 elemento na lista 

"""

def busca(lista, liminf, limsup, num):
    """ Busca um valor em uma lista, avaliando sempre a metade
    de um intervalo. Toda vez que atualizamos um limintante, descartamos 
    metade das possibilidades. Dividir log2(n) vezes para achar o valor"
    """
    if liminf == limsup and lista[liminf] != num:
        return -1
    else:
        m = (liminf + limsup) // 2  #o // aredondar a divisão para baixo
        
        if lista [m] == num:
            return m
        elif lista[m] < num:
            liminf = m + 1
            return busca(lista, liminf, limsup, num)
        else:
            limsup = m - 1
            return busca(lista, liminf, limsup, num)

def main():
    lista = input().split()
    num = int(input())

    for i in range(len(lista)):
        lista[i] = int(lista[i])

    contador = 0 
    print(busca(lista, 0, len(lista), num))

main()