"""
Lista de DICTS

"""

def criar_dicionario():
    """cria um dicionário vazio"""
    return []

def criar_verbete(palavra, classe, definicao, ano):
    """ Cria um novo verbete"""
    verbete = {
        "palavra": palavra, 
        "classe": classe, 
        "definicao": nova_definicao, 
        "ano":ano
    }
    return verbete

def adicionar_verbete(dicionario, verbete):
    """ adiciona um novo verbete ao dicionário
    é importante avisar o erro quando o dicionarista tenta adicionar
    um verbete já existente"""
    
    i = procurar_indice(dicionario, verbete["palavra"])
    if i is None:
        dicionario.append(verbete)
    else:
        raise Exception(f'A palavra {verbete["palavra"]} já existe.')   #cria uma nova exceção, sinalizando o erro 

def procurar_verbete(dicionario, palavra):
    """ devolve o verbete correspondente à palavra;
    se palavra não for encontrada, devolve None"""
    for verbete in dicionario:
        if verbete["palavra"] == palavra:
            return verbete 
    return None

def procurar_indice(dicionario, palavra):
    """ devolve o índice de uma palavra no dicionário
    ou None se ela não existir """
    for i, verbete in enumerate(dicionario):
        if verbete["palavra"] == palavra:
            return i
    return None

def atualizar_verbete(dicionario, verbete_atualizado):
    """ altera o verbete correspondente a uma palavra """
    idx = procurar_indice(dicionario, verbete_atualizado["palavra"])

    if idx == None: #se essa palavra não existir, basta adicioná-la ao fim da lista dicionário
        dicionario.append(verbete_atualizado)
    else:   #caso a palavra já exista em uma posição i, devemos atualizar a tupla que já continha a palavra
        dicionario[idx] = verbete_atualizado


def atualizar_definicao(dicionario, palavra, nova_definicao):   #não é possível alterar tuplas, devemos criar uma nova tupla
    """ atualiza a definicao de uma palavra""" 
    i = procurar_indice(dicionario, palavra)
    verbete_antigo = dicionario[i]
    #cria novo verbete
    verbete_atualizado = criar_verbete(
                            verbete_antigo["palavra"],
                            verbete_antigo["classe"], 
                            nova_definicao, 
                            verbete_antigo["ano"]
                        )

    dicionario[i] = verbete_atualizado
    # é mais simples atualizar a definição simplesmente por verbete_antigo["definicao"] = nova_definicao, 
    #isso faz o antigo e o novo verbete serem o mesmo objeto, oq impossibilita acessar a definição antiga 

def remover_verbete(dicionario, verbete):
    """ remove um verbete do dicionário"""
    idx = procurar_indice(dicionario, verbete["palavra"])
    dicionario.pop(idx)


def main():
    dicionario = criar_dicionario()

    verbete = {
        "palavra":"amor", 
        "classe":"substantivo", 
        "definicao": "fogo que arde sem se ver", 
        "ano":1595
    }
    
    adicionar_verbete(dicionario, verbete)

    verbete = procurar_verbete(dicionario, "amor")
    print(f'{verbete["palavra"]} significa {verbete["definicao"]}')
 
    nova_definicao = str(input("O que você acha que é amor?\n"))
    atualizar_definicao(dicionario, "amor", nova_definicao)

    verbete_atual = procurar_verbete(dicionario, "amor")  
    print(f'{verbete_atual["palavra"]} agora significa {verbete_atual["definicao"]}')
    print(f'{verbete["palavra"]} significava {verbete["definicao"]}')   #linha 78
    
    apelido = verbete
    #verifica se é igual, se tem o mesmo valor 
    if apelido == verbete:
        print("apelido e verbete são iguais")
    else:
        print("apelido e verbete são iguais")

    if verbete_atual == verbete:
        print("verbete atual e antigo são iguais")
    else:
        print("verbete atual e antigo NÃO são iguais")

    #verifica se é o mesmo objeto na memória (pode ser verificado por id)
    if apelido is verbete:
        print("apelido e verbete são o mesmo objeto")
    else:
        print("apelido e verbete não são o mesmo objeto")

    if verbete_atual is verbete:
        print("verbete atual e antigo são o mesmo objeto")
    else:
        print("verbete atual e antigo NÃO são o mesmo objeto")
        #duas variáveis podem ter o mesmo valor, mas não serem o mesmo objeto

    verbete = procurar_verbete(dicionario, "fogo")
    if verbete is None:
        print("A palavra fogo não está no dicionário")
    else:
        print(f'Fogo significa {verbete["definicao"]}')
main() 


