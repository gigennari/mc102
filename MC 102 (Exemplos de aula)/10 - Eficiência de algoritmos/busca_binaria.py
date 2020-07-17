"""
Usado para lista ordenadas; conjutos
Mas basta coonhecermos os limitates inf e sup da estrutura 
É mais eficiente que a busca sequencial
"""

def busca_binaria(lista, valor_procurado):
    """ Busca um valor em uma lista, avaliando sempre a metade
    de um intervalo. Toda vez que atualizamos um limintante, descartamos 
    metade das possibilidades. Dividir log2(n) vezes para achar o valor"
    """
    limitante_inferior = 0
    limitante_superior = len(lista)     
    while limitante_inferior <= limitante_superior:
        m = (limitante_inferior + limitante_superior) // 2  #o // aredondar a divisão para baixo
        if lista [m] == valor_procurado:
            return m
        elif lista[m] < valor_procurado:
            limitante_inferior = m + 1
        else:
            limitante_inferior = m - 1

