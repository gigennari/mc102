"""
É mais eficiente calcular um histograma usando dicionarios 

histograma = {'ana': 2, 'daniel': 10, 'gabriel': 20}

"""

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        lista = []
        for linha in arquivo:
            lista.append(int(linha.strip()))
    return lista

def calcular_histograma(lista):
    histograma = {}
    for elemento in lista:  #para cada item da lista 
        if elemento not in histograma:  #se o elemento está no histograma        
               histograma[elemento] = 0    #criar uma nova chave 
        
        histograma[elemento] += 1 #incremente o valor associado ao item

    return histograma


def main():
    dados1 = [1, 2, 7, 3, 2, 2, 6, 2, 1, 6]
    histograma1 = calcular_histograma(dados1)
    dados2 = ler_arquivo("grande.txt")
    histograma2 = calcular_histograma(dados2)
    print(histograma1)
    

main()