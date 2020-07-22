"""
Dada uma sequência de número não necessariamente ordenada, 
o programa encontra o k-ésimo menor elemento recursivamente


Entrada: sequencia de numeros; numero k
12 58 6 4 2 5 1
6

Saída: k-ésimo menor elemento da sequencia
12

Problema:

verificando toda a lista, deve haver k-1 elementos menores do que ele

então, queremos encontrar, a cada recursão o menor elemento de uma lista
quando tivermos repetido o procedimento k vezes, teremos o k-esimo menor 
da lista


Teremos uma função contadora 

se contador == k, devolve lista[k]
caso contrário, encontre o mínimo 

E outra função mínimo 
Caso básico: 
len(lista) == 1, o mínimo é o único elemento

Outros casos:
chamar novamente a função para calcular o minimo do restante da lista
comparamos número excluido com numero atual
se numero atual for menor que o anterior, atulizar minimo
devolve minimo


"""

def encontrar_minimo(lista):
    """Econtra o menor numero em uma lista"""
    if len(lista) == 1:
        return lista[0]
    else:
        minimo = lista[0]
        minimoatual = encontrar_minimo(lista[1:])
        if minimoatual < minimo:
            minimo = minimoatual
        else:
            encontrar_minimo(lista[1:])
        return minimo


def contador(lista, k):
    """Conta quantas vezes encotramos o valor mínimo de uma lista"""
    contador = 0
    listaordem = []

    for i in range(k):
        contador += 1
        menor = encontrar_minimo(lista)
        listaordem.append(menor)
        lista.remove(min(lista))
        
    if contador == k:
            return listaordem[k-1]
    

def main():
    lista = input().split()
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    k = int(input())


    print(contador(lista, k))

main()