"""
Lê um arquivo chamado palvras.txt e cria outros dois:

-um arquivo plural.txt com as palavras que terminam em s 
-um arquivo singular.txt com as demais 

"""

def ler_palavras(nome_arquivo):
    """ Lê o arquivo e devolve uma lista de palavras contidas nele """   
    with open(nome_arquivo) as arquivo: #o with fechar automaticamente o arquivo 
        palavras = []  #criar lista vazia 
        for linha in arquivo:   #percorrer lista do arquivo
            palavra = linha.strip() #descobrir palavra da linha 
            palavras.append(palavra)    #adicionar palavra a nova lista 
    return palavras     #devolver lista 

def separar_plurais(palavras):
    """ Devolve uma lista de palavras somentes com as palavras terminadas em s"""
    plurais = []
    for palavra in palavras:
        if palavra[-1] == 's':
            plurais.append(palavra)
    return plurais

def calcular_diferenca(lista1, lista2):
    """ Devolve os elementos da lista 1 que não estão na lista 2"""
    diferenca = []
    for palavra in lista1:
        if palavra not in lista2:
            diferenca.append(palavra)
    return diferenca


def criar_arquivo_palavras(nome_arquivo, palavras):
    """ Cria um arquivo de nome nome_arquivo com as palavras, uma por 
    linha """
    with open(nome_arquivo, "w") as arquivo:
        for palavra in palavras:
            linha = palavra + "\n"  #precisamos adicionar uma quebra de linha manualmente 
            arquivo.write(linha)
    return arquivo
    
def main():
    #ler as palavras do arquivo de entrada 
    palavras = ler_palavras("palavras.txt")
    #separar as que terminam em s 
    plurais = separar_plurais(palavras)
    #separar as demais 
    singulares = calcular_diferenca(palavras, plurais)
    #criar um arquivo plural.txt 
        # com as primeiras
    criar_arquivo_palavras("plural.txt", plurais)
    
    #cria um arquivo singular.txt
        #com as demais 
    criar_arquivo_palavras("singular.txt", singulares)
    print(plurais)

main()