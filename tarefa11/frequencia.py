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
def ler_arquivo_texto(nome_do_arquivo):
    """ lê o arquivo com todas as palavras do texto e as add a
    um dicionário?"""
    pass

def descobrir_frequencias(texto, stopwords):
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
    texto = ler_arquivo_texto(nome_do_arquivo)  #1ª entrada
    stopwords = ler_arquivo_texto(nome_do_arquivo)    #2ª entrada
    wordcount = descobrir_frequencias(texto, stopwords)
    tres_palavras = encontrar_mais_frequentes(wordcount)
    quartil_especial, palavras_eliminadas = calcular_quartil_especial(wordcount)
    tres_palavras_eliminadas = encontrar_mais_frequentes
    
    #printar as 3 palavras mais frequentes
    #printar len do quartil especial
    #printar 3 palavras eliminadas do quartil

main() 
