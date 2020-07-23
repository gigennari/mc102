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

def criar_arvore(urlinicial, urlbase, urlatual, lista_validas, lista_printadas):

    urlatual = obter_html(urlinicial) #função do módulo, devolve str
    
    lista_validas = validar_urls(urlatual)

    impressao_recursiva(lista_validas, lista_printadas, 0)
    

def validar_urls(urlatual):

    #href/regex
    href = [""] 
    padrao = r'href="(.*?)"'    #padrão do regex; ? nongreedy
    
    #re.findall()
    lista_todas = re.findall(padrao, urlatual)      

    #verficar se todas a urls são válidas --> lista_validas
    lista_validas = []
    for url in lista_todas:
        if eh_url_valida(url, urlatual): #se for uma url válida (exclui, por exemplos, links para o youtube e outros sites)
            lista_validas.append(url)   #add à lista de urls válidas

    return lista_validas
            

def impressao_recursiva(lista_validas, lista_printadas, contador):

    if contador == len(lista_validas):
        urlinicial = lista_validas[contador]
        lista_validas = []
        return criar_arvore(urlinicial, urlbase, urlatual, lista_validas, lista_printadas)
    else:
        for i, url in enumerate(lista_validas):
            if nao_visitado(url, lista_printadas):
                print(2 * contador * ' ' + url)
                lista_printadas.append(url)
                novaurl = lista_validas[contador]
                contador += 1
            impressao_recursiva(lista_validas, lista_printadas, contador)


def nao_visitado(url, lista_printadas):
    """Procura se um url já foi visitado e registrado na árvore"""
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