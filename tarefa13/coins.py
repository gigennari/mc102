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

Fazer em dict levou MUITO TEMPO para executar; vou fazer por lista e printar dentro das funções

"""

import sys

def calcular_notas(valor, notas):
    """Calcula quantas cédulas cabem em um valor, com a menor quantidade de células. Printa quantas cédulas são necessárias
    de cada valor e devolve valor menor que 2 reais para ser dividido em moedas""" 
 
    while valor > 2.00:
        for nota in notas:
            quantas_cabem = valor // nota
            valor -= quantas_cabem * nota
            if quantas_cabem >= 1:
                print(f"{int(quantas_cabem)} nota(s) de R$ {nota:.2f}")

    return valor

def calcular_moedas(valor, moedas):
    """Vê quais moedas podem decompor um valor, com a menor quantidade possível de moedas;
    printa a quantidade de moedas de cada valor""" 


    if valor > 1:
            valor -= 1
            print(f"1 moeda(s) de R$ 1.00")

    while valor > 0.00:
        for moeda in moedas:    
            quantas_cabem = valor // moeda
            valor -= quantas_cabem * moeda
            if quantas_cabem >= 1:
                print(f"{int(quantas_cabem)} moeda(s) de R$ {moeda:.2f}")
    
    return 


def main():
    valor = float(input())
    
    notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
    moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

    print("NOTAS:")
    restante = calcular_notas(valor, notas) 

    if restante > 0:
        print("MOEDAS:")
        moedas = calcular_moedas(restante, moedas)
    else:
        sys.exit()

main()