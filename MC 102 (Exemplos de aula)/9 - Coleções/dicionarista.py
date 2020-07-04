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
    for i, verbete in enumerate(dicionario):
        if verbete[0] == palavra:
            return i
    return None
    
def atualizar_definicao(dicionario, palavra, nova_definicao):   #não é possível alterar tuplas, devemos criar uma nova tupla
    """ atualiza a definição de uma palavra""" 
    i = procurar_indice(dicionario, palavra)
    verbete_antigo = dicionario[i]
    verbete_novo = (verbete_antigo[0], nova_definicao, verbete_antigo[2])
    dicionario[i] = verbete_novo

def remover_verbete(dicionario, verbete):
    idx = procurar_indice(dicionario, verbete[0])
    dicionario.pop(idx)

def main():
    dicionario = criar_dicionario()

    verbete = ("amor", "fogo que arde sem se ver", 1595)
    adicionar_verbete(dicionario, verbete)

    verbete = procurar_verbete(dicionario, "amor")
    palavra, definicao, ano  = verbete
    print(f'{palavra} significa {definicao}')

    nova_definicao = input("O que você acha que é amor?\n")
    atualizar_definicao(dicionario, "amor", nova_definicao)

    palavra, definicao, ano = procurar_verbete(dicionario, "amor")
    print(f"{palavra} agora significa {definicao}")

main() 



