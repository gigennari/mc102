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

and lista_todas[i] not in lista_printadas

"""

import re 
from modulo import*

def validar_urls(urlbase, urlatual, lista_printadas):
    """ Cria padrão regex, encontra todas as urls de uma página e resolve e valida cada uma"""
    htmlatual = obter_html(urlbase) #função do módulo, devolve str

    #href/regex
    href = [""] 
    padrao = r'"(.*?)"'    #padrão do regex; nongreedy
    
    #re.findall()
    lista_todas = re.findall(padrao, htmlatual)      

    #verficar se todas a urls são válidas --> lista_validas
    lista_validas = [] 
    for i in range(len(lista_todas)):
        lista_todas[i] = resolver_url(lista_todas[i], urlbase)
        if eh_url_valida(lista_todas[i], urlbase):
            lista_validas.append(lista_todas[i])   #add à lista de urls válidas   
    return lista_validas

def impressao_recursiva(urlbase, lista_validas, lista_printadas, lista_ramificada, contador):
    """ Printa as urls que ainda não foram printadas. Quando toda a lista de urls válidas já foi percorrida, chama criar árvore. """

    for i, j in enumerate(lista_validas):
        '''
        if i == 0 and j not in lista_printadas:
            lista_ramificada.append(j)
            lista_printadas.append(j)
            novos_validos = validar_urls(urlbase, j, lista_printadas)
            if len(novos_validos) != 0:
                impressao_recursiva(urlbase, novos_validos, lista_printadas, lista_ramificada, contador + 2) 
        '''    

        if j not in lista_printadas:
            lista_ramificada.append(2*contador*' ' + j)
            lista_printadas.append(j)
            novos_validos = validar_urls(urlbase, j, lista_printadas)
            if len(novos_validos) != 0:
                impressao_recursiva(urlbase, novos_validos, lista_printadas, lista_ramificada, contador + 1) 
                
    return lista_ramificada 

def main():
    urlinicial = input()

    lista_printadas = []
    lista_validas = validar_urls(urlinicial, urlinicial, lista_printadas)
    urlbase = urlinicial
       #acumula todas as url já printadas na tela para evitar repetição
    lista_ramificada = []
    arvore = impressao_recursiva(urlbase, lista_validas, lista_printadas, lista_ramificada, 0)

    for i in arvore:
        print(i)

main()