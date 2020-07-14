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
        print(entrada)
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
    pass

def calcular_quartil(wordcount):
    pass 


def calcular_quartil_especial(wordcount):
    """devolve as palavras cuja frequencia soma 25%, removidas as palavras 
    cujas frequencias são <= 5; essa palavras são devolvidas em um outro dict"""
    pass

def encontrar_mais_frequentes(dicionario):
    pass


def main():
    nome_do_arquivo, stopwords = ler_entrada()  #recebe caminho do arquivo e lista de stopwords
    palavras = ler_arquivo_texto(str(nome_do_arquivo).strip('[]').replace("'", ""))     
    wordcount = descobrir_frequencias(palavras, stopwords)
    tres_palavras = encontrar_mais_frequentes(wordcount)
    quartil_especial, palavras_eliminadas = calcular_quartil_especial(wordcount)
    tres_palavras_eliminadas = encontrar_mais_frequentes
    
    #printar as 3 palavras mais frequentes
    #printar len do quartil especial
    #printar 3 palavras eliminadas do quartil

main() 
