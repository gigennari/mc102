""" Um coelho está a dois metros de sua esposa.
Para chegar até ela, ele salta uma vez a cada minuto.
Primeiro salto de um metro, depois de meio metro, depois
de um quarto de metro e assim por diante (pg, com q=1/2).
Em quanto tempo ele chegara até ela?"""


def tempo_gasto_coelho():
    """ Enquanto a distância do coelho não for de 2 
    metros, ele salta uma distância de uma pg com
    o primeiro elemento igual a 1 e razõa 1/2.
    A cada salto o tempo é incrementado de um"""

    numero_saltos = 0  #numero de saltos = tempo em minutos; inicialização
    distância = 0
    proximo_salto = 1

    while distância < 2:    #floats tem um precisão finita, então chega em 2; condição
        numero_saltos += 1      #atualização
        distância += proximo_salto
        proximo_salto = proximo_salto / 2

    return numero_saltos

def main():
    tempo = tempo_gasto_coelho()
    print(f"O coelho gasta {tempo} minutos")

main()