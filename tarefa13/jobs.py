"""

ENTRADA:
numero de tarefas em linhas pares
grau de dificuldade de cada tarefa nas linhas ímpares
3
5 4 2


SAÍDA:
menor diferença possível entre o grau de dificuldade das tarefas
1

Ideia:
Percorrer toda a lista e somar todos os elemetos --> peso total
Criar uma lista vazia de comparação 
Criar uma variável acumuladora

Percorrer a lista novamente; a cada elemento, soma ele à variável acumuladora 
Faz a diferença entre peso total menos o elemento atual
e variável acumuladora

Devolve o menor valor da lista de comparação 

"""


def comparacao(n, pesos):
    """ Compara os pesos de n atividades e devolve a menor diferença possível"""
    peso_total = 0
    for i in range(n):
        peso_total += int(pesos[i])

    lista_comparativa = []
    acumuladora = 0

    for i in range(n):  #na última iteração será 0 
        acumuladora += int(pesos[i])
        peso_total -= int(pesos[i])
        diferenca = abs(peso_total - acumuladora)
        lista_comparativa.append(diferenca)

    menor = lista_comparativa[0]
    for diferenca in lista_comparativa:
        if diferenca < menor:
            menor = diferenca

    return menor
    

def ler_entrada():
    """Lê entrada, sendo uma linha com 1 número n e a seguinte com n números"""
    lista = []
    while True:
        try:
            n = int(input())
            lista.append(n)
            pesos = input().split()
            lista.append(pesos)
        except EOFError:
            return lista


def main():
    lista = ler_entrada()

    for i in range(0, len(lista), 2):   #como as linhas vem aos pares, pular de duas em duas 
        diferenca = comparacao(lista[i], lista[i+1])
        print(diferenca)


main()