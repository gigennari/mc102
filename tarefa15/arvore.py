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

Solução: fazer tudo na mesma função 

"""

import re 
from modulo import*

def criar_arvore(url_inicial, url_atual, url_base, lista_printadas, nivel):
    """ Printa a url de uma página inicial e toda a hierarquia das páginas que podem ser acessadas a partir da página inicial
    recursivamente. O recuo da impressão é controlado pelo nível da hierarquia.""" 

    #html do url atual passado como parâmetro
    htmlatual = obter_html(url_atual) #função do módulo, devolve str

    #href/regex -- > identifica links com o padrão html
    href = [""] 
    padrao = r'href="(.*?)"'    #padrão do regex; nongreedy
    
    #re.findall() --> devolve uma lista com todos os links presentes em uma página inicial, que satisfazem o padrão regex
    lista_todos = re.findall(padrao, htmlatual)

    #resolve e valida as urls da lista_todos; caso uma url já tenha sido printada, ela não será printada novamente pois está em lista_printadas
    for url in lista_todos:
        url = resolver_url(url, url_base)
        if eh_url_valida(url, url_inicial) and url not in lista_printadas:
            lista_printadas.append(url)
            print(f"{nivel*'  '}{url}")
            criar_arvore(url_inicial, url, url, lista_printadas, nivel+1)   #quando há links dentro um link, o recuo aumenta a partir do nível atual; 
                                                                            #ao esgotar essa lista, continua a anterior do recuo 'nivel' em que parou

def main():
    #recebe url da página inicial de um site 
    url_inicial = input()   

    #para a primeira recursão, o url_base e o url_atual são iguais ao input
    url_base = url_inicial  
    url_atual = url_inicial

    lista_printadas = []   #acumula todas as url já printadas na tela para evitar repetição
    nivel = 0   #a hierarquia começa no nivel 0

    criar_arvore(url_inicial, url_atual, url_base, lista_printadas, nivel)

main()