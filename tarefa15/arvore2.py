"""
Tentativa 2

O que eu preciso fazer:


1) pegar o html do link inicial 
2) econtrar todos os links válidos na página inicial 
3) printar esses primeiros link válidos

a) ao printar, add na lista_printados
b) aumentar o numero de espaços p o proximo link 
c) verficar se, dentro desse link, há outros links 
d) caso haja e caso eles ainda não tenham sido printados, chamar a função que printa 
caso contrário, continuar printando links da primeira lista 

"""

import re
from modulo import *


def criar_arvore(urlinicial, urlbase, url, lista_validos, lista_printados):

    dict_validos = {}
    for url in lista_validos:
        sublinks = encontrar_html_e_links_validos(urlinicial, urlbase, url, lista_printados)
        dict_validos[url] = sublinks

    imprimir(dict_validos, 0, lista_printados)


def encontrar_html_e_links_validos(urlinicial, urlbase, url, lista_printados):

    #obter html 
    html = obter_html(url)

    #href/regex
    href = [""] 
    padrao = r'href="(.*?)"'    #padrão do regex; nongreedy
    
    #re.findall()
    lista_todos = re.findall(padrao, html)     

    #resolver as urls e verificar se são válidas 
    lista_validos = []
    for link in lista_todos:
        link = resolver_url(link, urlbase)
        if eh_url_valida(link, urlinicial) and link not in lista_printados:
            lista_validos.append(link) 

    return lista_validos


def imprimir(dict_validos, contador, lista_printados):

    urls = dict_validos.keys()

    for url in urls:
        if url not in lista_printados:
            print(2*contador*' '+url)
            lista_printados.append(url)
            if len(dict_validos[url]) != 0:
                contador += 1
                imprimir2(dict_validos[url], contador, lista_printados)
            else:
                continue 


def imprimir2(lista, contador, lista_printados):
    for url in lista:
        if url not in lista_printados:
            print(2*contador*' '+url)
            lista_printados.append(url)
            contador += 1

def main():
    urlinicial = input()

    urlbase = urlinicial
    url = urlinicial
    lista_printados = []
    lista_validos = encontrar_html_e_links_validos(urlinicial, urlbase, url, lista_printados)

    criar_arvore(urlinicial, urlbase, url, lista_validos, lista_printados)

main()