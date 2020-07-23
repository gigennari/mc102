"""
O programa árvore.py recebe uma URL correspondente à uma página inicial. 
Ele chama as funções do modulo para acessar os links dessa página inicial 
que redirecionam para outras páginas. 

Na árvore, há todos os links acessáveis, na ordem em que aparecem. Os links 
só devem ser acessados se estiverem contidos no mesmo subdiretório. 

O programa, antes de adicionar um link à árvore, verfica se eles estão no 
mesmo subdiretório e se o link não foi acessado antes.

Dúvida 1: como fazer a "quebra" da árvore quando muda a tag?
Dúvida 2: Não está acessando os links dentro da página fixacao do teste 1

"""

import re 
from modulo import*

def criar_arvore(urlinicial, urlbase, urlatual, lista_validas, lista_printadas):
    """Recebe a url inicial, converte para hatml, chama a função validar urls e depois imprime recursivamente as urls"""

    htmlatual = obter_html(urlinicial) #função do módulo, devolve str
    
    lista_validas = validar_urls(urlinicial, urlbase, htmlatual)

    contador = 0
    impressao_recursiva(lista_validas, lista_printadas, contador)
    

def validar_urls(urlinicial, urlbase, urlatual):
    """ Cria padrão regex, encontra todas as urls de uma página e resolve e valida cada uma"""

    #href/regex
    href = [""] 
    padrao = r'href="(.*?)"'    #padrão do regex; nongreedy
    
    #re.findall()
    lista_todas = re.findall(padrao, urlatual)      

    #verficar se todas a urls são válidas --> lista_validas
    lista_validas = [] 
    for i in range(len(lista_todas)):
        lista_todas[i] = resolver_url(lista_todas[i], urlbase)
        if eh_url_valida(lista_todas[i], urlinicial): #se for uma url válida (exclui, por exemplos, links para o youtube e outros sites)
            lista_validas.append(lista_todas[i])   #add à lista de urls válidas
    return lista_validas
            

def impressao_recursiva(lista_validas, lista_printadas, contador):
    """ Printa as urls que ainda não foram printadas. Quando toda a lista de urls válidas já foi percorrida, chama criar árvore. """

    if contador == len(lista_validas):
        urlbase = lista_validas[contador]   #qual url passar? 
        lista_validas = []
        return criar_arvore(urlinicial, urlbase, urlatual, lista_validas, lista_printadas)
    else:
        for i, url in enumerate(lista_validas):
            if nao_visitado(url, lista_printadas):
                print(2 * contador * ' ' + url)
                lista_printadas.append(url)
                contador += 1
                
                impressao_recursiva(lista_validas, lista_printadas, contador)

       
def nao_visitado(url, lista_printadas):
    """Procura se um url já foi visitado e printado na árvore"""
    if url not in lista_printadas:
        return True
    else:
        return False 


def main():
    urlinicial = input()

    urlatual = urlinicial   #deve ser alterado pelo regex assim que receber
    urlbase = urlinicial 
    lista_printadas = []   #acumula todas as url já printadas na tela para evitar repetição
    lista_validas = []
    arvore = criar_arvore(urlinicial, urlbase, urlatual, lista_validas, lista_printadas)

main()