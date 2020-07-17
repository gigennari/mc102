"""
removi da função encontrar mais frequentes
"""

if wc[2][1] == wc[3][1]:
        restante = wc[2:]
        mesma_freq = [wc[2]]
        for i in range(len(restante)-1):
            if restante[i][1] == restante[i+1][1]:  #deixa apenas tuplas que tem a mesma frequencia da 3ª palavra
                mesma_freq.append(restante[i+1])
            else:
                break 
        mesma_freq = dict(mesma_freq)
        mesma_freq_ordem_alfabetica = sorted(mesma_freq, key=lambda x: x[0]) 
        tres_palavras.append(mesma_freq_ordem_alfabetica[0])     
    else:
        tres_palavras.append(wc[2][0]) 

def ordenar(wc, tres_palavras):
    
    if wc[0][1] == wc[1][1] == wc [2][1]:
        tres_palavras_ordem = sorted(tres_palavras) 
    elif wc[0][1] == wc [1][1]: #ordenar as duas primeiras 
        tres_palavras_ordem = []
        terceira = tres_palavras[2]
        lista = sorted(tres_palavras[:2])
        for palavra in lista:
            tres_palavras_ordem.append(palavra)
        tres_palavras_ordem.append(terceira)
    elif wc[1][1] == wc [2][1]:   #ordenar as duas últimas palavras em ordem alfabética, caso tenham mesma freq
            tres_palavras_ordem = []
            tres_palavras_ordem.append(tres_palavras[0])
            restante = tres_palavras[1:]
            lista = sorted(restante)
            for palavra in lista:
                tres_palavras_ordem.append(palavra)
    else:
        tres_palavras_ordem = tres_palavras
    return tres_palavras_ordem


     