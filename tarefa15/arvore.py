"""
O programa árvore.py recebe uma URL correspondente à uma página inicial. 
Ele chama as funções do modulo para acessar os links dessa página inicial 
que redirecionam para outras páginas. 

Na árvore, há todos os links acessáveis, na ordem em que aparecem. Os links 
só devem ser acessados se estiverem contidos no mesmo subdiretório. Ou seja,
de

podemos ir para 

mas não para 


O programa, antes de adicionar um link à árvore, verfica se eles estão no 
mesmo subdiretório e se o link não foi acessado antes.
"""

import re 
from modulo import*

def criar_arvore(urlbase, urlatual, lista_validas, lista_arvore, recuo):

    html_url_atual = obter_html(urlinicial) #função do módulo, devolve str
    
    #href/regex

    #re.findall()

    #verficar se todas a urls são válidas --> lista_validas

    for i, url in enumerate(lista_validas):

        if subdiretorio_igual() and nao_visitado(url, lista_arvore):
            recuo += "  "
            print(recuo+url)
            lista_arvore.append(url, lista_arvore)    #registrar todas as urls já visitadas
        else:
            urlatual = lista_validas[i]
            criar_arvore(urlbase, urlatual, lista_validas, lista_arvore, recuo)


def subdiretorio_igual(urlatual, urlencontrado):
    """Verifica se um link encontrado está no mesmo subdiretório do link atual"""
    pass

def nao_visitado(url, lista_arvore):
    """Procura se um url já foi visitado e registrado na árvore"""
    pass


def main():
    urlinicial = input()

    arvore = criar_arvore()

main()