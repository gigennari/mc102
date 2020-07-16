"""
Escreva um programa que, dado um arquivo de texto, conte a frequência com que elas 
aparecem no texto e descubra algumas palavras-chaves do texto.

As palavras mais frequentes dão uma boa ideia do tópico principal

As stop words não devem ser incluídas na contagem (artigos, preposiçãoes
conectivos, etc)

Entrada:
uma linha contendo o caminho de um arquivo
uma linha contendo stop words

Saída:
1ª linha - as 3 palavras mais frequentes, da mais à menos frequente
2ª linha - número de palavras cuja freq é >= à da última palavra do 1º
quartil (a soma da frequencia das palavras do primeiro quartil é 25% do total
de palavras), OU SEJA, QUANTAS PALAVRAS correspodem ao conjunto de palavras 
que mais aparecem, somando uma frequência de 25% 

para formar o quartil, DESCONSIDERA até três palavras m
Para resolver empates --> usar ordem lexicográfica (alfabética)


"""
import string 
import math

def ler_entrada():
    entrada = []
    while True:
        try:
            aqr_ou_palavra = input().split()
            entrada.append(aqr_ou_palavra)
        except EOFError: 
            break 
    return entrada

def ler_arquivo_texto(nome_do_arquivo):
    """ lê o arquivo com todas as palavras do texto e as add a
    um dicionário?"""
    texto = open(nome_do_arquivo).read().lower()
    for pontuacao in string.punctuation:    #remover pontuação
        texto = texto.replace(pontuacao, ' ')
    palavras = texto.split()
    return palavras

def descobrir_frequencias(palavras, stopwords):
    """ contar a frequencia de cada uma das palavras, eliminadas
    as stopwords """ 
    wordcount = {}  #vamos usar um dict para armazenar a palavra e sua frequencia juntos
    palavras_interesse = [p for p in palavras if p not in stopwords] #aqui ainda é preciso usar lista para saber a frequencia

    for palavra in palavras_interesse:
        if palavra in wordcount:
            wordcount[palavra] += 1
        else:
            wordcount[palavra] = 1
    return wordcount


def calcular_quartil_especial(wc):
    """remove as palavras cujas frequencias são <= 5 e devolve as palavras 
    1/4 da lista restante; essa palavras são devolvidas em um outro dict"""
    lista_tuplas = []
    frequencia_alta = []
    quartil = []
    
    for i in wc:    #transforma wc em uma lista de tuplas (palavra, freq)
        tupla = (i, wc[i])
        lista_tuplas.append(tupla)

    for i in range(len(lista_tuplas)):  #mantém apenas palavras que se repetem mais que 5 vezes
        if lista_tuplas[i][1] > 5:  
            frequencia_alta.append(lista_tuplas[i])

    N = len(frequencia_alta)
    Q14 = math.floor(0.25 * (N+1))
    quartil = frequencia_alta[:Q14]

    return len(quartil)

def encontrar_mais_frequentes(wc):
    """ encontra as três mais palavras mais frequentes; a entrada é uma 
    lista de tuplas """
    tres_palavras = [wc[0][0], wc[1][0]]   
    
    if wc[2][1] == wc[3][1]:
        restante = wc[2:]
        mesma_freq = [wc[2]]
        for i in range(len(restante)-1):
            if restante[i][1] == restante[i+1][1]:  #deixa apenas tuplas que tem a mesma frequencia da 3ª palavra
                mesma_freq.append(restante[i+1])
            else:
                break 
        mesma_freq = dict(mesma_freq)
        mesma_freq_ordem_alfabetica = sorted(mesma_freq, key=lambda x: x[0])  #não esta colocando em ordem alfabetica
        
        tres_palavras.append(mesma_freq_ordem_alfabetica[0]) 
    else:
        tres_palavras.append(wc[2][0]) 
    return tres_palavras


def main():
    nome_do_arquivo, stopwords = ler_entrada()  #recebe caminho do arquivo e lista de stopwords
    palavras = ler_arquivo_texto(str(nome_do_arquivo).strip('[]').replace("'", ""))     
    wordcount = descobrir_frequencias(palavras, stopwords)
    wordcount_ordenado = sorted(wordcount.items(), key = lambda x: x[1],reverse=True )  #gera uma lista de tuplas
    tres_palavras = encontrar_mais_frequentes(wordcount_ordenado)
    len_quartil = calcular_quartil_especial(wordcount)
    tres_palavras_eliminadas = encontrar_mais_frequentes(wordcount_ordenado[len_quartil:])

    print(wordcount_ordenado)

    print(str(tres_palavras).strip('[]').replace("'", "").replace(",", ""))  #printar as 3 palavras mais frequentes/ converter str
    print(len_quartil)    #printar len do quartil especial
    print(str(sorted(tres_palavras_eliminadas)).strip('[]').replace("'", "").replace(",", "")) #printar 3 palavras eliminadas do quartil/ converter str 

main() 
