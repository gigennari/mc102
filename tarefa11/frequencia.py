"""
Escreva um porograma que, dado um arquivo de texto, conte a frequência com que elas 
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

