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

def limpar_pontuacao(string):

    pontuacao = ".,;:?!''/*#@&" #sem hifen
    sem_pontucao = ""

    for letra in string:
        if letra not in pontuacao:
            sem_pontucao += letra
    
    return sem_pontucao

def ler_arquivo_texto(nome_do_arquivo):
    """ lê o arquivo com todas as palavras do texto e as add a
    um dicionário?"""
    texto = open(nome_do_arquivo).read().lower()
    
    texto = limpar_pontuacao(texto)
           
    palavras = texto.split()
    return palavras

def descobrir_frequencias(palavras, stopwords):
    """ contar a frequencia de cada uma das palavras, eliminadas
    as stopwords; devolve dict """ 
    wordcount = {}  #vamos usar um dict para armazenar a palavra e sua frequencia juntos
    palavras_interesse = [p for p in palavras if p not in stopwords] #aqui ainda é preciso usar lista para saber a frequencia

    for palavra in palavras_interesse:
        if palavra in wordcount:
            wordcount[palavra] += 1
        else:
            wordcount[palavra] = 1
    return wordcount

def ordenar_wc(wordcount):
    """ ordena em ordem alfabética e frequência"""  #evitou ter que tratar cada caso na hora de encontrar os três elementos de maior frequencia 
        
    wco = sorted(wordcount.items(), key=lambda a: a[0])  #devolve uma lista de tuplas (palavra, frequencia) em ordem alfabérica

    wco.sort(key=lambda f: f[1], reverse=True)    #ordena a lista em ordem crescente 

    return wco

def calcular_quartil_especial(wc):
    """remove as palavras cujas frequencias são <= 5 e devolve as palavras 
    1/4 da lista restante; essa palavras são devolvidas em um outro dict"""
    frequencia_alta = []

    for i in range(len(wc)):  #mantém apenas palavras que se repetem mais que 5 vezes
        if wc[i][1] > 5:  
            frequencia_alta.append(wc[i])      

    N = len(frequencia_alta)
    Q14 = round(0.25 * (N+1))
    depois_quartil = frequencia_alta[Q14:]
    valor = frequencia_alta[Q14-1][1]   #é a frequencia do último elemento do quartil Q14 - 1 pq a lista começa no 0
    contador = Q14  #com certeza já há Q14 elementos (do quartil) que têm freq igual ou maior à do último elemento
    
    for i in range(len(depois_quartil)):    #queremos verificar se os próximos números, depois do quartil, tem a mesma freq do último
        if depois_quartil[i][1] == valor:
            contador += 1
        else:
            break
    return contador

def encontrar_mais_frequentes(wc):
    """ encontra as três mais palavras mais frequentes; a entrada é uma 
    lista de tuplas """
    tres_palavras = [wc[0][0], wc[1][0], wc[2][0]]  

    return tres_palavras


def main():
    nome_do_arquivo, stopwords = ler_entrada()  #recebe caminho do arquivo e lista de stopwords
    palavras = ler_arquivo_texto(str(nome_do_arquivo).strip('[]').replace("'", ""))     
    wordcount = descobrir_frequencias(palavras, stopwords)
    wordcount_ordenado = ordenar_wc(wordcount) #gera uma lista de tuplas

    tres_palavras = encontrar_mais_frequentes(wordcount_ordenado)
    len_quartil = calcular_quartil_especial(wordcount_ordenado)
    tres_palavras_eliminadas = encontrar_mais_frequentes(wordcount_ordenado[len_quartil:])

    print(str(tres_palavras).strip('[]').replace("'", "").replace(",", ""))  #printar as 3 palavras mais frequentes/ converter str
    print(len_quartil)    #printar len do quartil especial
    print(str(tres_palavras_eliminadas).strip('[]').replace("'", "").replace(",", "")) #printar 3 palavras eliminadas do quartil/ converter str 

main() 
