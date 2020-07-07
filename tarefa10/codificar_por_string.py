
def codificar(largura, altura, imagem):
    """ Parte de uma matriz com linhas de 0 e 1 e escrevea imagem no formato PBM """ 
    codificacao = ''
    lista_codificacao = []
    string_todos_bits = '' 
    str_bits_pares = ''
    str_bits_impares = ''
    lista_frequencia = []
    lista_pares_finais = []

    for i in range(altura):
        string = str(imagem[i]).strip().replace("'", "")
        string_todos_bits = string_todos_bits + string 
    
    vezes = int(len(string_todos_bits) / 8)
    k = 0
    for i in range(vezes+1):
        bits_pares = string_todos_bits[i+k: i+k+8].strip(' ')
        str_bits_pares = str_bits_pares + bits_pares
       
        bits_impares = string_todos_bits[i+k+8 : i+k+17].strip(' ')
        str_bits_impares = str_bits_impares + bits_impares
        k += 16

    tuplas = list(zip(str_bits_pares, str_bits_impares))

    contador = 1
    for i in range(len(tuplas)-1): 
        if i <= len(tuplas):
            if tuplas[i][0] == tuplas[i+1][0] and tuplas[i][1] == tuplas[i+1][1]:
                contador += 1
                proximo_igual = True 
                if i == len(tuplas) - 2:
                    if tuplas[-1] == tuplas[-2] and proximo_igual:
                        lista_frequencia.append(contador)
                        lista_pares_finais.append(tuplas[-1])
                    elif tuplas[-1] != tuplas [-2] and proximo_igual:
                        lista_frequencia.append(contador)
                        lista_frequencia.append(tuplas[-3])
                        lista_frequencia.append(1)
                        lista_pares_finais.append(tuplas[-1])
                    elif not proximo_igual:
                        if tuplas[-1] == tuplas[-2]:
                            lista_frequencia.append(contador)
                            lista_frequencia.append(tuplas[-3])
                            lista_frequencia.append(2)
                            lista_pares_finais.append(tuplas[-1])
                        else:           #tuplas[-1] != tuplas [-2] 
                            lista_frequencia.append(contador)
                            lista_frequencia.append(tuplas[-3])
                            lista_frequencia.append(1)
                            lista_pares_finais.append(tuplas[-2])
                            lista_frequencia.append(1)
                            lista_pares_finais.append(tuplas[-1])
            else:
                lista_frequencia.append(contador)
                contador = 1
                lista_pares_finais.append(tuplas[i-1])
        
    for y in range(len(lista_frequencia)):
        lista_codificacao.append(lista_frequencia[y])
        par_bits = lista_pares_finais[y][0] + lista_pares_finais[y][1]
        lista_codificacao.append(par_bits)  
    for elemento in lista_codificacao:
        codificacao = codificacao + str(elemento) + ' ' 
    return codificacao


def decodificar(largura, altura, codificacao):
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
