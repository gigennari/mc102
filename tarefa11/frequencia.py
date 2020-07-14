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

para formar o quartil, DESCONSIDERAR palavras que se repetem 5 vezes ou menos

3ª linha - até 3 palavras mais frequentes entre aquelas que não foram 
incluídas na contagem da linha anterior, OU SEJA, as 3 palavras com maior 
frequencia q estariam no quartil, mas se repetem 5 vezes ou menos, então 
foram excluídas

Para resolver empates --> usar ordem lexicográfica (alfabética)


"""
import string 

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

def calcular_quartil(wordcount):
    pass 


def calcular_quartil_especial(wordcount):
    """devolve as palavras cuja frequencia soma 25%, removidas as palavras 
    cujas frequencias são <= 5; essa palavras são devolvidas em um outro dict"""
    pass

def encontrar_mais_frequentes(wordcount_ordenado):
    """ encontra as três mais palavras mais frequentes; a entrada é uma 
    lista de tuplas """
    tres_palavras = []
    tres_palavras.append(wordcount_ordenado[0][0])
    tres_palavras.append(wordcount_ordenado[1][0])
    if wordcount_ordenado[2][1] == wordcount_ordenado[3][1]:
        restante = dict(wordcount_ordenado[2:])
        restante_ordem_alfabetica = sorted(restante.items(), key=lambda x: x[0], reverse=True)
        tres_palavras.append(restante_ordem_alfabetica[0][0])
    else:
        tres_palavras.append(wordcount_ordenado[2][0])
    return tres_palavras


def main():
    nome_do_arquivo, stopwords = ler_entrada()  #recebe caminho do arquivo e lista de stopwords
    palavras = ler_arquivo_texto(str(nome_do_arquivo).strip('[]').replace("'", ""))     
    wordcount = descobrir_frequencias(palavras, stopwords)
    wordcount_ordenado = sorted(wordcount.items(), key = lambda x: x[1],reverse=True )  #gera uma lista de tuplas
    tres_palavras = encontrar_mais_frequentes(wordcount_ordenado)
    
    quartil_especial, palavras_eliminadas = calcular_quartil_especial(wordcount)
    tres_palavras_eliminadas = encontrar_mais_frequentes
    
    print(tres_palavras)
    #printar as 3 palavras mais frequentes
    #printar len do quartil especial
    #printar 3 palavras eliminadas do quartil

main() 
