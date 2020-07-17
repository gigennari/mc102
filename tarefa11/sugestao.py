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
    def __init__(self, palavra, classe, definicao, ano, sinonimos):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


def ler_entrada():
    """lê caminho do texto e duas palavras do texto por linha, formando uma lista de Frase""" 
    pass

def ler_arquivo_texto():
    """lê arquivo de texto, chama função para limpar pontuação e transforma em lista"""
    pass

def limpar_pontuacao(string):

    pontuacao = ".,;:?!''/*#@&" #sem hifen
    sem_pontucao = ""

    for letra in string:
        if letra not in pontuacao:
            sem_pontucao += letra
    
    return sem_pontucao

def encontrar_proxima_palavra():
    """procura todas as próximas palavras, adiciona em uma lista, conta frequencia (dict),  frase.p3 = palavra de maior frequencia;
    a mais frequente será a próxima"""



def main():
    caminho, duplas = ler_entrada
    frases = ler_arquivo_texto(caminho)
    trios = encontrar_proxima_palavra(palavras, frases)

main()