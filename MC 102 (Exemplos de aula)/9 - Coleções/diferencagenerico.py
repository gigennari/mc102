"""

Escreva uma função que receba dois conjuntos de strings e devolva
a diferença entre esses conjuntos 

Queremos tirar a diferença entre as 1000 palavras mais faladas 
em portugues e e em espanhol para verificar se de fato os idiomas 
são parecidos 


"""

def ler_palavras_frequentes(nome_arquivo, n):
    """lê o arquivo de frequência de palavras e 
    devolve as n palavras mais frequentes"""

    lista = []
    with open(nome_arquivo) as arquivo:
        i = 0 
        for linha in arquivo:
            lista.append(linha.strip())
            i += 1
            of i == n:
                break   
    return lista

def calcular_diferenca(a,b):
    """recebe conjuntos a e b e devolve a - b """
    diferenca = []
    for elemento_a in a:
        if elemento_a not in b:
            diferenca.append(elemento_a)
    return diferenca

def main():
    palavras_pt = ler_palavras_frequentes(pt_br.txt, 10)
    palavras_es = ler_palavras_frequentes(es.txt, 10)
    diferenca = calcular_diferenca(a,b)    
    print(diferenca)   

main()