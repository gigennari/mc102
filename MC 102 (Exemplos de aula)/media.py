"""
Enunciando:
Leia um conjunto de notas de provas e devolva
a média das notas que tiverem valor maior ou igual a 5.

Entrada: uma linha para o número de notas e
depois uma linha para cada nota 

Saída: a média com uma casal decimal das notas maiores que 5. 
Caso não haja notas maiores que cinco, palavra 'erro'. 

Algoritmo: 

#leia um número n
#lista de notas <-- leia n números de ponto flutuante 
#cópia das notas maiores que 5 
#calcular a média dos valores 
"""
#leia um número n
n = int(input('Quantas notas gostaria de inserir? '))         

#lista de notas <-- leia n números de ponto flutuante 
i=0 
lista_de_notas = []
while i<n:
    nota = float((input('Insira a nota: ')))
    lista_de_notas.append(nota)
    i += 1

#cópia das notas maiores que 5 
notas_maiores = []
for nota in lista_de_notas:
    if nota >= 5:
        notas_maiores.append(nota)

#calcular a média dos valores 
soma_notas_maiores = 0
media = 0
if len(notas_maiores) != 0:
    for nota in notas_maiores:
        soma_notas_maiores += nota
    media = soma_notas_maiores / len(notas_maiores)
    print(f'A média das notas é {media:.1f}')      #devolve média com uma casa decimal 
else:
    print('Erro')