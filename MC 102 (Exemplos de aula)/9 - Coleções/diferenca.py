"""

Escreva uma função que receba dois conjuntos de strings e devolva
a diferença entre essesc onjuntos 

"""

def calcular_diferenca(a,b):
    """recebe conjuntos a e b e devolve a - b """
    diferenca = []
    for elemento_a in a:
        if elemento_a not in b:
            diferenca.append(elemento_a)
    return diferenca

def main():
    a = ["ana", "maria", "pedro", "felipe"] 
    b = ["lucas", "gustavo", "maria", "ana"]
    diferenca = calcular_diferenca(a,b)    
    print(diferenca)

main()