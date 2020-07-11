
def codificar(largura, altura, imagem):
    """ Parte de uma matriz com linhas de 0 e 1 e escrevea imagem no formato PBM """ 
    lista_codificacao = []
    codificacao = ''
    lista_todos = []
    lista_frequencia = []
    lista_pares_finais = []
    contador = 0
    
    for i in range(0, altura, 2):   #i é linha
        for j in range(largura):    #j é coluna
            bit_cima = imagem[i][j]
            bit_baixo = imagem[i+1][j]
            par = str(bit_cima) + str(bit_baixo)
            lista_todos.append(par)
    
    contador = 1
    for i in range(len(lista_todos)-1):
        if i <= len(lista_todos):
            if lista_todos[i] == lista_todos[i+1]:
                contador += 1
                proximo_igual = True 
                if i == (len(lista_todos) - 2):
                    if lista_todos[-1] == lista_todos[-2] and proximo_igual:    #3 últimos iguais (A, A, A)
                        lista_frequencia.append(contador)
                        lista_pares_finais.append(lista_todos[-1])
                    elif lista_todos[-1] != lista_todos[-2] and proximo_igual: # A, A, B
                        lista_frequencia.append(contador)
                        lista_frequencia.append(lista_todos[-3])   
                        lista_frequencia.append(1)
                        lista_pares_finais.append(lista_todos[-1])  
                    elif not proximo_igual: #se o penúltimo é diferente do antepenúltimo, o antepenúltimo já está nas listas freq/par
                        if lista_todos[-1] == lista_todos[-2]: #A, B, B
                            lista_frequencia.append(2)
                            lista_pares_finais.append(lista_todos[-1])
                        else: #A, B, C
                            lista_frequencia.append(1)
                            lista_pares_finais.append(lista_todos[-2])
                            lista_frequencia.append(1)
                            lista_pares_finais.append(lista_todos[-1])
            else:
                lista_frequencia.append(contador)
                lista_pares_finais.append(lista_todos[i])
                contador = 1
         
    for i in range(len(lista_frequencia)):
        lista_codificacao.append(str(lista_frequencia[i]))
        lista_codificacao.append(lista_pares_finais[i])
    
    for elemento in lista_codificacao:
        codificacao += str(elemento) + ' ' 
        codificacao = str(codificacao)
        
    return codificacao

def decodificar(largura, altura, codificacao):
    todos_os_bits = []  #todos os bits da codificacao
    bits_pares = []     #todos os bits pares, que estarão em linhas pares
    bits_impares = []   #todos os bits impares que estarão em linhas impares
    linhas_pares = []
    linhas_impares = []
    imagem = []
    for i, numero in enumerate(codificacao):
        if i % 2 == 0:
            frequencia = int(numero) * codificacao[i+1]
            todos_os_bits.append(frequencia)
    for i, bit in enumerate(todos_os_bits):
        if i % 2 == 0:
            bits_pares.append(bit)
        else:
            bits_impares.append(bit)
    k = 0
    for _ in range(bits_pares, 8):
        linha = bits_pares[k:k+8]
        linhas_pares.append(linha)
        k += 8
    l = 0    
    for _ in range(bits_impares, 8):
        linha = bits_pares[l:l+8]
        linhas_impares.append(linha)
        l += 8
   
    linha_atual = []
    for i in range(altura):
        for j in range(largura, 8):
            if j % 2 == 0:
                byte = bits_pares[((i+1)*j)-1]
                linha_atual.append(byte)
            else:
                byte = bits_impares[(i*j)-1]
                linha_atual.append(byte)
            imagem.append(linha_atual)
        linha_atual = []   

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
        linha1 = 'P1C' '\n'
        arquivo.write(linha1)
        linha2 = str(largura) + ' ' + str(altura) + '\n'
        arquivo.write(linha2)
        linha3 = ''
        for elemento in codificacao:
            linha3 += str(elemento) + ' '
        arquivo.write(linha3.strip())       
    return arquivo



def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as arquivo:
        for sequencia in imagem:
            linha = sequencia + '\n'
            arquivo.write(linha)
    return arquivo