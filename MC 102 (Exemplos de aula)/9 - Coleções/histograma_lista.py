"""
Crie um programa que calcule o histograma de um 
conjunto de numeros 

Dados: 1 2 1 3 2 2 6 2 1 


Conjunto de tuplas (numero, frequencia) ??
conj = {(1, 3), (2, 4), (3, 1), (6,2)}
Mas não sabemos essas frequencias de cara e não conseguimos 
alterar uma tupla nem acessar ela se estiver em um conjunto 

Então, vamos usar uma lista de listas 
[[1, 0], [2, 0], [3, 0)], [6, 0]]

Percorrendo os i dados, 
    se o elemento já for o primeiro elemento de uma das listas da lista (elemento = lista[i][0])
        incrementar a frequencia do numero (lista[i][1] += 1)
    caso contrário:
        adicionar à lista de listas, uma nova lista com o numero e frequencia 1 (lista.append([dados[i], 1]))


"""
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        lista = []
        for linha in arquivo:
            lista.append(int(linha.strip()))
    return lista

def calcular_histograma(dados):
    histograma = []
    for item in dados:
        for par in histograma:  #lento
            if par[0] == item:
                break
        else:
            par = [item, 0]
            histograma.append(par)
        
        par[1] += 1
    return histograma


def main():
    dados1 = [1, 2, 7, 3, 2, 2, 6, 2, 1, 6]
    histograma1 = calcular_histograma(dados1)
    dados2 = ler_arquivo("grande.txt")
    histograma2 = calcular_histograma(dados2)
    for i in range(len(histograma1)):
        print(f"O número {histograma1[i][0]} aparece {histograma1[i][1]} vezes")
    print(histograma2)

main()