
def codificar(largura, altura, imagem):
    """ Parte de uma matriz com linhas de 0 e 1 e escrevea imagem no formato PBM """ 
    lista_todos = []
    codificacao = []
    contador = 0
    
    for i in range(0, altura, 2):   #i é linha
        for j in range(largura):    #j é coluna
            bit_cima = imagem[i][j]
            bit_baixo = imagem[i+1][j]
            par = str(bit_cima) + str(bit_baixo)
            lista_todos.append(par)
    
    contador = 1
    for i in range(1, len(lista_todos)): #comparar "de trás p frente" -- resolveu o problema com o último elemento no teste disquete
        if i < len(lista_todos)-1:  #comparar até o penúltimo com o antepenúltimo
            if lista_todos[i] == lista_todos[i-1]:
                contador += 1
            else:
                codificacao.append(contador)
                codificacao.append(lista_todos[i-1])
                contador = 1
                
        else:                                             #i == (len(lista_todos) - 1); comparar último com penúltimo apenas; aqui contador = frequencia do penúltimo
                if lista_todos[-1] == lista_todos[-2]:    
                    codificacao.append(contador+1)
                    codificacao.append(lista_todos[-1])
                else:                                     # lista_todos[-1] != lista_todos[-2]:
                    codificacao.append(contador)
                    codificacao.append(lista_todos[-2])   
                    codificacao.append(1)
                    codificacao.append(lista_todos[-1])              
   
    return codificacao

def decodificar(largura, altura, codificacao):
    todos_os_bits = []  #todos os bits da codificacao
    imagem = [[0 for coluna in range(largura)] for linha in range(altura)] 
    
    for y in range(0, len(codificacao), 2):
        for _ in range(int(codificacao[y])):
            todos_os_bits.append(codificacao[y+1])  #aqui temos uma lista do tipo ['01', '01', '01', '01', '00']

    k = 0
    for i in range(0, altura, 2):
        for j in range(largura):
            imagem[i][j] = todos_os_bits[k+j][0]
            imagem[i+1][j] = todos_os_bits[k+j][1]
        k+= largura

    return imagem


def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        linhas = []
        for linha in arquivo:
            linhas.append(linha.strip())  #linha 0 - P1c; linha 1 - altura largura; linha 2 - matriz 
    largura, altura = linhas[1].split()
    largura = int(largura)
    altura = int(altura)
    codificacao = [numero for numero in linhas[2].split()]

    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):     
    with open(nome_do_arquivo) as arquivo:
        tipo = arquivo.readline()
        largura_altura = arquivo.readline().strip().split()
        imagem = []
        for linha in arquivo:
            imagem.append(list(linha.strip()))
    largura = len(imagem[0])
    altura = len(imagem)    

    return largura, altura, imagem


def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as arquivo:
        arquivo.write('P1C' '\n')
        arquivo.write(str(largura) + ' ' + str(altura) + '\n')
        linha3 = ''
        for i in codificacao:
            linha3 += str(i) + ' '
        arquivo.write(linha3)       
    return arquivo


def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as arquivo:
        arquivo.write('P1''\n')
        arquivo.write(str(largura) + ' ' + str(altura) + '\n')
        for i in range(altura):    #a imagem é uma matriz 
            for j in range(largura):
                arquivo.write(str(imagem[i][j]))
            arquivo.write('\n') #no final de cada linha, quebra de linha
        
    return arquivo