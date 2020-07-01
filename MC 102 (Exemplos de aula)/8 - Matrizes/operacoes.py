
def soma_matrizes(A, B):
    """soma duas matrizes"""
    m = len(A) #numero de linhas
    n = len(A[0]) #numero de colunas
    soma = []

    for i in range(m):                  #para i de 0 até m-1:
        linha = []                      #crie uma linha de soma 
        soma.append(linha)              #inclua na variável soma   
        for j in range(n):              #para j de 0 até n-1:
            celula = A[i][j] + B[i][j]  #calcula a célula = a[i][j] + b[i][j]
            linha.append(celula)        #inclua celula na linha
    return soma


def produto_matrizes(A, B):
    m = len(A) #numero de linhas de A
    l = len(A[0])   #numero de colunas de A ou numero de linhas de B, supondo entrada váida
    n = len(B[0])   #numero de colunas de B
    C = [[0 for _ in range(n)] for _ in range (m)]  # cria matriz C de dimensões m por n
    for i in range(m):  #para cada linha de C
        for j in range(n):  #para cada coluna de C 
            v = produto_interno(A, B, i, j)    #calcula o produto interno de linha de A e coluna de B 
            C[i][j] = v #Cij recebe valor produto interno
    return C


def produto_interno(A, B, i, j): 
    """ multiplica a i-ésima linha de A pela j-ésima coluna de B"""
    linha = A[i]
    coluna = []
    m = len(linha) #quanitidade de elemntos na linha tem que ser igual na coluna e qtde de multiplicaçoes que faremos     
    for x in range(m): #para cada linha de B 
        elemento = B[x][j]  #econtrar o elemento da coluna j
        coluna.append(elemento)
    produto_interno = 0
    for y in range(m):
        produto = linha[y] * coluna[y]
        produto_interno += produto
    return produto_interno 



    pass

def matriz_transposta(A):

    pass

def matriz_inversa(A):
    pass


def main():

    turma_a = [ [5.3, 4.0, 7.5], 
                [10.0, 0.0, 9.5], 
                [7.0, 6.9, 7.8]]
    
    turma_b = [ [1.0, 0.0, 0.0], 
                [0.0, 1.0, 0.0], 
                [0.0, 0.0, 1.0]]   

    soma = soma_matrizes(turma_a, turma_b)
    produto = produto_matrizes(turma_a, turma_b)
    print(soma)
    print(produto)

main() 