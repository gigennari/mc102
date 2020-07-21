"""
O progama determina o número mínimo de movimentos necessários
para resolver o problema da torre de Hanói com n discos.

Entrada: um inteiro n
2
Saída:nº mínimo de movimentos 
3

O problema:

Três estacas A, B e C
N discos na estaca A; todos devem ser movidos para a estaca C

Regras:
Apenas um disco pode ser movido de cada vez
Um disco só pode ser colocado sobre um disco maior 
Queremos realizar o menor numero de movimentos possível

Caso básico: se só temos 1 disco, mover para estaca C
Forma mais rápida de resolver: A --> B ; A -->C; --> B -->C
Queremos mover n-1 discos da estaca A para a estaca B, usando a C como auxliar
para depois transferir o maior disco para a estaca C


Note que a torre de hanoi segue a função 
f(1) = 1
f(2) = 3
f(3) = 7
f(4) = 15

Ou seja, y = 2^x - 1

Mas devemos resolver recursivamente

Os prints dos movimentos a serem feitos foi removido para não interferir no programa, 
mas fica auqui o registro 
primeiro_movimento = hanoi(n-1, origem, auxiliar, destino, contador)  
            print(f"Mova o disco {n} de {origem} para {destino}")
            segundo_movimento = hanoi(1, origem, destino, auxiliar, contador) 
            print(f"Mova o disco {n} de {origem} para {destino}")
            terceiro_movimento = hanoi(n-1, auxiliar, destino, origem, contador) 
            print(f"Mova o disco {n} de {origem} para {destino}")
            return primeiro_movimento + segundo_movimento + terceiro_movimento

"""

def hanoi(n, origem, destino, auxiliar, contador):
    """ Imprime quantos movimentos são necessários para mover n discos da estaca
    A para a estaca C com a ajuda da estaca B"""
    if n > 0:
        if n == 1:
            return 1
        else:

            primeiro_movimento = hanoi(n-1, origem, auxiliar, destino, contador)  
            segundo_movimento = hanoi(1, origem, destino, auxiliar, contador) 
            terceiro_movimento = hanoi(n-1, auxiliar, destino, origem, contador) 
            return primeiro_movimento + segundo_movimento + terceiro_movimento
            
        
    return(contador)



def main():
    numero_discos = int(input())
    contador = 0
    
    print(hanoi(numero_discos, 'A', 'B', 'C', contador))

main()