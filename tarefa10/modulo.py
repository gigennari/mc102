
def codificar(largura, altura, imagem):
    """ Parte de uma matriz com linhas de 0 e 1 e escrevea imagem no formato PBM """ 
    codificacao = []
    
    string_todos_bits = '' 
    str_bits_pares = ''
    str_bits_impares = ''

    for i in range(altura):
        string = str(imagem[i]).strip().replace("'", "")
        string_todos_bits = string_todos_bits + string 
    
    for digito in string_todos_bits:
        bits_pares = string_todos_bits[i: i+8].strip(' ')
        str_bits_pares = str_bits_pares + bits_pares
        bits_impares = string_todos_bits[i+8 : i+16].strip(' ')
        str_bits_impares = str_bits_impares + bits_impares
        
    for i in range(len(bits_pares)):
        str_atual = str(bits_pares[i]).strip('[]').replace("'", "")
        str_bits_pares = str_bits_pares + str_atual

    for i in range(len(bits_impares)):
        str_atual = str(bits_impares[i]).strip('[]').replace("'", "")
        str_bits_impares = str_bits_impares + str_atual
    
    num_pares = largura * 2
    lista_frequencia = []
    lista_pares_finais = []

    print(str_bits_pares)
    print(str_bits_impares)
    

    tuplas = list(zip(str_bits_pares, str_bits_impares))
    print(tuplas)
    contador = 1
    for i in range(len(tuplas)-1): 
        if i-2 <= len(tuplas):
            if tuplas[i][0] == tuplas[i+1][0] and tuplas[i][1] == tuplas[i+1][1]:
                contador += 1
            else:
                lista_frequencia.append(contador)
                contador = 1
                lista_pares_finais.append(tuplas[i-1])
        
    for y in range(len(lista_frequencia)):
        codificacao.append(lista_frequencia[y])
        par_bits = int(lista_pares_finais[y][0] + lista_pares_finais[y][1])
        codificacao.append(par_bits)  
    
    return codificacao


def decodificar(largura, altura, codificacao):
    print(codificacao)
    todos_os_bits = []  #todos os bits da codificacao
    bits_pares = []     #todos os bits pares, que estarão em linhas pares
    bits_impares = []   #todos os bits impares que estarão em linhas impares
    linhas_pares = []
    linhas_impares = []
    imagem = []
    for numero in codificacao:
        if numero % 2 == 0:
            sequencia = numero * codificacao[numero+1]
            todos_os_bits.append(sequencia)
    for i, bit in enumerate(todos_os_bits):
        if i % 2 == 0:
            bits_pares.append(bit)
        else:
            bits_impares.append(bit)
    for i in bits_pares:
        linha = bits_pares[i:i+8]
        linhas_pares.append(linha)
    for i in bits_impares:
        linha = bits_pares[i:i+8]
        linhas_impares.append(linha)
    linha_atual = []
    for i in range(altura):
        for j in range(largura):
            if j % 2 == 0:
                byte = bits_pares[(i*j)-1]
                linha_atual.append(byte)
            else:
                byte = bits_impares[(i*j)-1]
                linha_atual.append(byte)
            imagem.append(linha_atual)
        linha_atual = []     
    return imagem


def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo, "r") as arquivo:
        tipo = arquivo.readline()
        largura_altura = arquivo.readline()
        codificacaostr = arquivo.readline()
        largura = largura_altura[0]
        altura = largura_altura[1]
    codificacao = list(codificacaostr)
    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):  
    with open(nome_do_arquivo, "r") as arquivo:
        tipo = arquivo.readline()
        largura_altura = arquivo.readline()
        imagem = []
        for linha in arquivo:
            linha_atual = linha.strip()
            imagem.append(linha_atual)
    arquivo.close()
    largura = int(largura_altura[0])
    altura = int(largura_altura[2])
    return largura, altura, imagem


def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as arquivo:
        linha1 = 'P1C' + '\n'
        arquivo.write(linha1)
        linha2 = str(altura) + str(largura) + '\n'
        arquivo.write(linha2)
        linha = ''
        for i in range(len(codificacao)):
            linha = linha + str(codificacao[i]).strip('[]').replace("'", "")
        linha3 = linha + '\n'
        arquivo.write(linha3)       
    return arquivo



def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as arquivo:
        for sequencia in imagem:
            linha = sequencia + '\n'
            arquivo.write(linha)
    return arquivo