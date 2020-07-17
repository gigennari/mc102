"""
Escreva um programa que, dadas duas palavras, sugere ao usuário qual será
a próxima palavra, tal que essa escolha seja baseada na probabilidade de que 
essas três palavras apareçam nessa ordem em um determinado texto.

Entrada:
1ª linha - o caminho do arquivo de texto
2ª linha - sequência de pares de palavras, um por linha 

Saída:
frase sugerida com 3 palavras, um trio por linha 

Exemplo:
E:
testes/tetxto0.in
buraco negro
buracos negros
campo gravitacional

S:
buraco negro é 
buracos negros não
campo gravitacional pode

Vamos criar uma classe com 3 palavras


"""

class Frase:  #cria uma nova classe de abstração; coleção fixa de propriedades
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def __repr__(self):  
        return "% s % s % s" % (self.p1, self.p2, self.p3)

def ler_entrada():
    """lê caminho do texto e duas palavras do texto por linha, formando uma lista de Frase""" 
    caminho = input()
    lista = []
    
    while True:
        try:
            palavras = input().split()
            frase = Frase(palavras[0], palavras[1], "")
            lista.append(frase)
        except EOFError: 
            break 
    return caminho, lista

def ler_arquivo_texto(nome_do_arquivo):
    """lê arquivo de texto, chama função para limpar pontuação e transforma em lista"""
    texto = open(nome_do_arquivo).read().lower()
    
    texto = limpar_pontuacao(texto)
           
    palavras = texto.split()
    return palavras

def limpar_pontuacao(string):

    pontuacao = ".,;:?!''/*#@&" #sem hifen
    sem_pontucao = ""

    for letra in string:
        if letra not in pontuacao:
            sem_pontucao += letra
    
    return sem_pontucao

def descobrir_frequencias(palavras):
    """ contar a frequencia de cada uma das palavras; devolve dict """ 
    wordcount = {}  #vamos usar um dict para armazenar a palavra e sua frequencia juntos
    
    for palavra in palavras:
        if palavra in wordcount:
            wordcount[palavra] += 1
        else:
            wordcount[palavra] = 1
    
    return wordcount

def encontrar_proxima_palavra(texto, frase):
    """procura todas as próximas palavras, adiciona em uma lista, conta frequencia (dict),  frase.p3 = palavra de maior frequencia;
    a mais frequente será a próxima"""

    proximas = []

    for i, palavra in enumerate(texto):   #procura próximas palavras 
        if texto[i] == frase.p1:
            if texto[i+1] == frase.p2:
                seguinte = texto[i+2]
                proximas.append(seguinte)   #adiciona todas as palavras que aparecem depois das duas primeiras

    #contar frequencia da lista --> dict --> dict.keys()
    proximas_dict = descobrir_frequencias(proximas)
       
    proximasordenadas = sorted(proximas_dict.items(), key=lambda a: a[0])  #devolve uma lista de tuplas (palavra, frequencia) em ordem alfabética

    proximasordenadas.sort(key=lambda f: f[1], reverse=True)    #ordena a lista em ordem decrescente 
    
    #frase.p3 = 1º elemento do dicionário 
    frase.p3 = proximasordenadas[0][0]

    return frase 


def main():
    caminho, frases = ler_entrada()
    texto = ler_arquivo_texto(caminho)
    trios = []
    for frase in frases:
        frase_completa = encontrar_proxima_palavra(texto, frase)
        trios.append(frase_completa)

    for frase in trios:
        print(frase)

main()