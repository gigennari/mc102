"""
Leia um número de ponto flutuante com DUAS casas decimais. 
Esse valor representa um valor monetário. A seguir, calcule o menor 
número de notas e moedas possíveis no qual o valor pode ser decomposto.

As notas consideradas são de 100, 50, 20, 10, 5, 2. 
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 

A seguir mostre a relação de notas e moedas necessárias.

Entrada: numero de ponto fluante (288,90)

Saída: 
NOTAS:
2 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
1 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
1 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.25
1 moeda(s) de R$ 0.10
1 moeda(s) de R$ 0.05

Note que 90 centavos poderia ser decomposto em 
1) 0.50, 0.25, 0.10, 0.05
2) 0.50, 0.10, 0.10, 0.10, 0.10
Ou seja, precisamos sempre achar o maior valor que cabe dentro do restante

O melhor jeito para acumular a quantidade de notas e moedas é usar
dois dicts, um para notas e um para moedas.

notas = {100.00: 0, 50.00:0, 25.00:0...}
moedas = {1.00:0, 0.50:0, 0.25:0...}

na hora de imprimir, se valor da chave for 0, passar

"""

def calcular_notas(valor, notas, moedas):
    """Vê quais notas podem decompor um valor inteiro e altera os valores
    do dict notas; devolve o dict""" 
    
    cedulas = notas.keys()

    while valor > 1.00:
        for cedula in cedulas:
            if valor / cedula < 1 :
                pass
            elif valor / cedula > 1:
                valor -= cedula
                notas[cedula] += 1

    if valor == 1:
        moedas[1.00] += 1   #caso o valor seja ímpar, precisamos add uma moeda de 1 real 

    return dict(notas), dict(moedas)

def calcular_moedas(valor, moedas):
      """Vê quais moedas podem decompor um valor e altera os valores
    do dict moedas; devolve o dict""" 

    moedas_disponiveis = moedas.keys()

    #como já adicionamos as moedas de 1 real na função calcular notas e o valor é, com certeza, inferior a 1 real, vamos eliminá-lo da lista
    moedas_disponiveis.pop(0)   #agora moedas_disponiveis = [0.50, 0.25, 0.10, 0.05, 0.01]

    while valor > 0.00:
        for moeda in moedas_disponiveis:    
            if (valor / moeda) < 1:
                pass
            elif valor / moeda > 1:
                valor -= moeda
                moedas[moeda] += 1

    return moedas

def main():
    valor = round(float(input()), 2)
    
    inteiro = int(valor)
    notas = {100.00: 0, 50.00:0, 20.00:0, 10.00:0, 5.00:0, 2.00:0}

    centavos = valor - inteiro
    moedas = {1.00:0, 0.50:0, 0.25:0, 0.10:0, 0.05:0, 0.01:0}

    notas, moedas = calcular_notas(inteiro, notas, moedas)  #caso o valor seja ímpar, precisamos adicionar uma moeda de 1 real --  passar dict moedas

    moedas = calcular_moedas(centavos, moedas)

    chaves_notas = notas.keys()
    chaves_moedas = moedas.keys()

    print("NOTAS:")
    for nota in chaves_notas:
        if notas[nota] == 0:
            pass
        else: 
            print(f"{notas[nota]} nota(s) de R$ {nota}")
    
    print("MOEDAS:")
    for moeda in chaves_moedas:
        if moedas[moeda] == 0:
            pass
        else: 
            print(f"{moedas[moeda]} moeda(s) de R$ {moeda}")

main()