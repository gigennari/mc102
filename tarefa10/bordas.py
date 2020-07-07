"""
A borda de um objeto é representada pelos pixels que que tem ao menos um vizinho que não está no objeto.

É uma matriz do tamanho da imagem, mas com 1 apenas na borda

"""

from modulo import *


def destacar_bordas(largura, altura, imagem):
    bordas = [[0 for _ in range(largura)] for _ in range (altura)]

    for i in range(altura): 
        for j in range(largura):  
            if (i == 1 or i == altura) and (j == 1 or j == largura):
                if imagem[i][j] == '1':
                    bordas[i][j] = '1'
            elif i == 1 and j!= 1 and j!= largura:
                if imagem[i][j] == '1':
                    bordas[i][j] = '1'
            elif i == altura and j!= 1 and j!= largura:
                if imagem[i][j] == '1':
                    bordas[i][j] = '1'
            elif j == 1 and i!= 1 and j!= altura:
                if imagem[i][j] == '1':
                    bordas[i][j] = '1'
            elif j == largura and i!= 1 and j!= altura:
                if imagem[i][j] == '1':
                    bordas[i][j] = '1'       
            elif (i != 1) and (i != altura) and (j != 1) and (j != largura):
                if imagem[i-1][j] == '1' and (imagem[i][j+1] == '0' or imagem[i][j-1] == '0' or imagem[i+1][j]== '0'):
                    bordas[i][j] = '1'
                elif imagem[i+1][j] == '1' and (imagem[i][j+1] == '0' or imagem[i][j-1] == '0' or imagem[i-1][j]== '0'):
                    bordas[i][j] = '1'
                elif imagem[i][j+1] == '1' and (imagem[i][j-1] == '0' or imagem[i+1][j] == '0' or imagem[i-1][j]== '0'):
                    bordas[i][j] = '1'
                elif imagem[i][j-1] == '1' and (imagem[i][j+1] == '0' or imagem[i+1][j] == '0' or imagem[i-1][j]== '0'):
                    bordas[i][j] = '1'
            

    return bordas


def main():

    arquivo_entrada = input()
    arquivo_saida = input()

    largura, altura, codificacao = carregar_imagem_codificada(arquivo_entrada)
    imagem = decodificar(largura, altura, codificacao)
    nova_imagem = destacar_bordas(largura, altura, imagem)

    codificacao = codificar(largura, altura, nova_imagem)
    escrever_imagem_codificada(largura, altura, codificacao, arquivo_saida)


if __name__ == '__main__':
    main()
