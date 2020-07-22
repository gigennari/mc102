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

Encontrar o mínimo recursivamente não funciona quando há muitos dados. 
Vamos fazer recursão para contador
se contador == 0:
devolver o último item da lista de indices 

caso contrário, chama a função novamente com uma lista menor e subtrair um do contador 

"""

def kesimo(lista, contador):
    """Conta quantas vezes encotramos o valor mínimo de uma lista"""

    if contador == 1:
        menor = lista[0]
        for numero in lista:
            if numero < menor:
                menor = numero
        return menor
    else:
        contador -= 1
        menor = lista[0]
        for numero in (lista):
            if numero < menor:
                menor = numero
        i = lista.index(menor)
        lista.pop(i)
        return kesimo(lista, contador)
                
        
def main():
    lista = input().split()
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    k = int(input())

    print(kesimo(lista, k))

main()