""" Escreva um programa que leia a nota de 10 exercícios 
de 3 alunos e depois:

a) calcule a média da TURMA de cada exercício
b) descubra o exercício com menor média
c) calcule  a média de cada ALUNO, excluindo-se
    o exercicio de menor média

"""

NUMERO_EXERCICIOS = 10
NUMERO_ALUNOS = 3

def ler_notas_exercicios(n):
    lista_notas = []
    for _ in range(n):
        nota = float(input())
        lista_notas.append(nota)
    return lista_notas

def ler_notas_alunos(m, n):    #m é o numero de alunos
    """ Lê a lista de notas de cada aluno e devolve"""
    listas_notas = []
    for _ in range(m):
        print('Digite as notas dos exercios próximo: ')
        lista_notas = ler_notas_exercicios(n)   #lista de um único aluno
        listas_notas.append(lista_notas)    #lista com m listas, cada uma com n notas
    return listas_notas 

def calcular_media_exercicios(notas_alunos): 
    """ Calcula a média de cada um dos exercícios e 
    devolve uma lista com as medias de todos os exercícios""" 
    m = len(notas_alunos) #numero de alunos
    n = len(notas_alunos[0])    #numero de exercícios
    media_exercicios = []
    
    for j in range(n):  #para cada j dos n exerícios
        soma = 0
        for i in range (m): #para cada i do m alunos 
            soma += soma + notas_alunos[i][j]    #adicione a soma da nota do exercício j do aluno i (i-ésimo aluno/j-ésima nota)
        media = soma / m
        media_exercicios.append(media)
    return media_exercicios

def obter_pior_exercicio(lista_medias):
    """Devolve o índice da menor media"""
    menor_nota = lista_medias[0]
    indice_menor = 0
    for i, nota in enumerate(lista_medias):
        if nota < menor_nota:
            menor_nota = nota
            indice_menor = i
    return indice_menor

def calcular_media_aluno(lista, idx):
    """Devolve a média das notas de um aluno, excluindo-se a nota de 
    indice i"""
    soma = 0.0
    for i, nota in enumerate(lista):
        if i != idx:
            soma += nota
    media = soma / (len(lista) -1)
    return media

def calcular_medias_turma(notas_alunos, idx):
    """ Para cada aluno, calcula a média dos exercícios
    dessa aluno. excluindo o de indice idx.
    Devolve as médias de todos os alunos"""
    medias = []
    for lista_notas in notas_alunos:
        media = calcular_media_aluno(lista_notas, idx)
        medias.append(media) 
    return medias

def main():
    notas_alunos = ler_notas_alunos(NUMERO_ALUNOS, NUMERO_EXERCICIOS) #ler a nota dos exercícios 
    media_exercicios = calcular_media_exercicios(notas_alunos)
    idx_pior = obter_pior_exercicio(media_exercicios)
    medias_turma = calcular_medias_turma(notas_alunos, idx_pior)
    print(medias_turma)

main()