"""
O programa árvore.py recebe uma URL correspondente à uma página inicial. 
Ele chama as funções do modulo para acessar os links dessa página inicial 
que redirecionam para outras páginas. 

Na árvore, há todos os links acessáveis, na ordem em que aparecem. Os links 
só devem ser acessados se estiverem contidos no mesmo subdiretório. 

O programa, antes de adicionar um link à árvore, verfica se eles estão no 
mesmo subdiretório e se o link não foi acessado antes.

^(https)(\:\/\/)([^\ ]+)    $
"""

import re 
from modulo import*

def criar_arvore(urlinicial, urlbase, urlatual, lista_validas, lista_arvore, recuo):

    urlatual = obter_html(urlinicial) #função do módulo, devolve str
    
    lista_validas = validar_urls()

    verificar_condicoes_e_imprimir()
    

def validar_urls(lista_todas, urlinicial, urlbase):
       
    lista_todas =            #como encontrar todas?

    #href/regex
    href = [""] 
    regex = r'href="(.*?)"' 
    
    #re.findall()
    lista_todas = re.findall(regex, lista_todas)      

    #verficar se todas a urls são válidas --> lista_validas
    lista_validas = []
    for url in lista_todas:
        if eh_url_valida(url, url_inicial): #se for uma url válida (exclui, por exemplos, links para o youtube e outros sites)
            lista_validas.append(url)   #add à lista de urls válidas

    return lista_validas

def verificar_condicoes_e_imprimir():
    
    #verficar se a url em lista_validas tem o mesmo subdiretório e ainda não foi printada
    for i, url in enumerate(lista_validas):

        if subdiretorio_igual() and nao_visitado(url, lista_arvore):
            recuo += "  "
            print(recuo+url)
            lista_arvore.append(url, lista_arvore)    #registrar todas as urls já visitadas
        else:
            urlatual = lista_validas[i]
            recuo = ""
            lista_validas = []
            return criar_arvore(urlinicial, urlbase, urlatual, lista_validas, lista_arvore, recuo)


def subdiretorio_igual(urlbase, url):
    """Verifica se um link encontrado está no mesmo subdiretório do link atual"""
    pass

def nao_visitado(url, lista_arvore):
    """Procura se um url já foi visitado e registrado na árvore"""
    if url not in lista_arvore:
        return True
    else:
        return False 


def main():
    urlinicial = input()

    urlatual = urlinicial   #deve ser alterado pelo regex assim que receber
    urlbase = urlinicial #deve ser alterado pelo regex assim que receber
    lista_arvore = []   #acumula todas as url já printadas na tela para evitar repetição
    recuo = ""  #não há espaçamento para o primeiro link
    arvore = criar_arvore(urlinicial, urlbase, urlatual, lista_arvore, recuo)

main()