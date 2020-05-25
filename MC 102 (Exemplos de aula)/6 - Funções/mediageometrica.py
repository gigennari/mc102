"""
Crie um programa que leia duas listas do teclado, correspondentes
às notas de provas e de exercícios dos estudantes, normaliza cada
nota dividindo-se a nota pelo máximo da lista correspondente e
computa a média final de cada estudante, que é dada pela média
geométrica (multiplicar as notas e extrair raiz com indicie igual ao 
numero de fatores, 2 no caso) entre a nota de prova e de exercícios.



Entrada:
Uma lista de nota de prova
Uma lista com notas de exercicios

Saída: 
Uma lista com a média geométrica das notas de cada aluno 
"""
import math 

def ler_notas(n, tipo):
    """ Lê uma lista de n numeros no teclado """
    print(f"Insira notas de {tipo}")
    lista = []
    for _ in range(n):
        nota = float(input())
        lista.append(nota)
    return lista

def normalizar_notas(lista):
    """ Encontra a maior nota da lista e 
    devolve uma nova lista com as notas normalizadas
    pela maior nota """
    maior_nota = lista[0]
    lista_normalizada = []
    for nota in lista:
        if nota > maior_nota:
            maior_nota = nota
        continue     #continue ou break? 
    for i in range(len(lista)):
        nota_normalizada = lista[i]/maior_nota
        lista_normalizada.append(nota_normalizada)
    return lista_normalizada


def calcular_medias_geometricas(lista1, lista2):
    """ Devolve uma nova lista com as médias 
    geométricas entre notas de prova e de
    exercício para cada aluno """
    lista = []
    for i in range(len(lista1)):
        media = math.sqrt(lista1[i] * lista2[i])
        lista.append(media)
    return lista


def main():
    n = int(input("Quantos alunos há? "))
    notas_provas = ler_notas(n, tipo='provas')     #ler notas de prova
    notas_exercicios = ler_notas(n, tipo='exercício')     #ler notas de exercicios
    notas_prova_normalizadas = normalizar_notas(notas_provas)       #normalizar_notas_prova
    notas_exercicios_normalizadas = normalizar_notas(notas_exercicios)        #normalizar_notas_exercicios 
    medias_geometricas = calcular_medias_geometricas(notas_prova_normalizadas, notas_exercicios_normalizadas)
    print(medias_geometricas)    #imrpiir médias geométricas
    
   

main()