"""

Dicionarista: 

-cataloga
    guardar um conjunto de palavras 
    manter essa lista atualizada 
    modificar as informações associadas

-classifica
    classificar a classe gramatical
    genero, numero

-define 
    definicao de cada palavra 


Queremos criar um programa que auxilie o dicionarista:
Como representar um dicionário? Como abstrair esse objeto em forma de uma estrutura de dados?

Uma lista de tuplas 
Tuplas --> (palavra, definicao, ano)

dict

-adicionar classe da palavra ao verbete: alterar a forma como representamos o verbete


Verbete = (palavra, classe, definição, ano)
"""
def criar_dicionario():
    """cria um dicionário vazio"""
    dicionario = []
    return dicionario

def adicionar_verbete(dicionario, verbete):
    """ adiciona um novo verbete ao dicionário
    é importante avisar o erro quando o dicionarista tenta adicionar
    um verbete já existente"""
    i = procurar_indice(dicionario, verbete[0])
    if i is None:
        dicionario.append(verbete)
    else:
        raise Exception(f"A palavra {verbete[0]} já existe.")   #cria uma nova exceção, sinalizando o erro 

def procurar_verbete(dicionario, palavra):
    """ devolve o verbete correspondente à palavra;
    se palavra não for encontrada, devolve None"""
    for verbete in dicionario:
        if verbete[0] == palavra:
            return verbete 
    return None

def procurar_indice(dicionario, palavra):
    """ devolve o índice de uma palavra no dicionário"""
    for i, verbete in enumerate(dicionario):
        if verbete[0] == palavra:
            return i
    return None

def atualizar_verbete(dicionario, verbete_atualizado):
    """ altera o verbete correspondente a uma palavra """
    idx = procurar_indice(dicionario, verbete_atualizado[0])

    if idx == None: #se essa palavra não existir, basta adicioná-la ao fim da lista dicionário
        dicionario.append(verbete_atualizado)
    else:   #caso a palavra já exista em uma posição i, devemos atualizar a tupla que já continha a palavra
        dicionario[idx] = verbete_atualizado


def atualizar_definicao(dicionario, palavra, nova_definicao):   #não é possível alterar tuplas, devemos criar uma nova tupla
    """ atualiza a definição de uma palavra""" 
    idx = procurar_indice(dicionario, palavra)
    verbete_antigo = dicionario[idx]
    verbete_novo = (verbete_antigo[0], verbete_antigo[1], nova_definicao, verbete_antigo[3])
    dicionario[idx] = verbete_novo

def remover_verbete(dicionario, verbete):
    """ remove um verbete do dicionário"""
    idx = procurar_indice(dicionario, verbete[0])
    dicionario.pop(idx)



def main():
    dicionario = criar_dicionario()

    verbete = ("amor", "substantivo", "fogo que arde sem se ver", 1595)
    adicionar_verbete(dicionario, verbete)

    verbete = procurar_verbete(dicionario, "amor")
    palavra, definicao, ano  = verbete
    print(f'{palavra} significa {definicao}')
 
    nova_definicao = input("O que você acha que é amor?\n")
    atualizar_definicao(dicionario, "amor", nova_definicao)

    palavra, classe, definicao, ano = procurar_verbete(dicionario, "amor")
    print(f"{palavra} agora significa {definicao}")
    
    verbete = procurar_verbete(dicionario, "fogo")
    if verbete is None:
        print("A palavra fogo não está no dicionário")
    else:
        print(f"Fogo significa {fogo[1]}")
main() 



