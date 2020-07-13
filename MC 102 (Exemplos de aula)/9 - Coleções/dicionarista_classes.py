"""
Classe = astração
Objeto = o valor do tipo dessa abstração
"""

class Verbete:  #cria uma nova classe de abstração; coleção fixa de propriedades
    def __init__(self, palavra, classe, definicao, ano, sinonimos):
        self.palavra = palavra
        self.classe = classe
        self.definicao = definicao
        self.ano = ano
        self.sinonimos = sinonimos

def criar_dicionario():
    """cria um dicionário vazio"""
    return []

def criar_verbete(palavra, classe, definicao, ano, sinonimos):
    """ Cria um novo verbete"""
    verbete = Verbete(palavra, classe, definicao, ano, sinonimos)
    return verbete

def adicionar_verbete(dicionario, verbete):
    """ adiciona um novo verbete ao dicionário
    é importante avisar o erro quando o dicionarista tenta adicionar
    um verbete já existente"""
    
    i = procurar_indice(dicionario, verbete.palavra)
    if i is None:
        dicionario.append(verbete)
    else:
        raise Exception(f'A palavra {verbete["palavra"]} já existe.')   #cria uma nova exceção, sinalizando o erro 

def procurar_verbete(dicionario, palavra):
    """ devolve o verbete correspondente à palavra;
    se palavra não for encontrada, devolve None"""
    for verbete in dicionario:
        if verbete.palavra == palavra:
            return verbete 
    return None

def procurar_indice(dicionario, palavra):
    """ devolve o índice de uma palavra no dicionário
    ou None se ela não existir """
    for i, verbete in enumerate(dicionario):
        if verbete.palavra == palavra:
            return i
    return None

def atualizar_verbete(dicionario, verbete_atualizado):
    """ susbstitui o verbete correspondente a uma palavra """
    idx = procurar_indice(dicionario, verbete_atualizado.palavra)

    if idx == None: #se essa palavra não existir, basta adicioná-la ao fim da lista dicionário
        dicionario.append(verbete_atualizado)
    else:   #caso a palavra já exista em uma posição i, devemos atualizar a tupla que já continha a palavra
        dicionario[idx] = verbete_atualizado

def atualizar_definicao(dicionario, palavra, nova_definicao):   

def main():
    dicionario = criar_dicionario()
    verbete = Verbete(
        "amor",
        "susbtantivo",
        "fogo que arde sem se ver",
        1540,
        ["sofrer", "cantar no chuveiro"]
    )   
    adicionar_verbete(dicionario, verbete)

    verbete = procurar_verbete(dicionario, "amor")
    print(f'{verbete.palavra} significa {verbete.definicao}')
 
    nova_definicao = str(input("O que você acha que é amor?\n"))
    atualizar_definicao(dicionario, "amor", nova_definicao)

    verbete_atual = procurar_verbete(dicionario, "amor")  
    print(f'{verbete_atual.palavra} agora significa {verbete_atual.definicao}')
    print(f'{verbete.palavra} significava {verbete.definicao}')  

main() 
