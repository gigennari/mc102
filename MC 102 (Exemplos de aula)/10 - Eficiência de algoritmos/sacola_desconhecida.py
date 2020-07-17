"""
No novo jogo:

1. A Diná irá criar uma lista de numeros que está ordenada
(ou seja, João não sabe quais são os números)

2. Para cada chute, Diná dirá se o número é menor ou maior que 
o numero pensado 

3. João deve adivinhar a posição do numero, não o número em si 

Chutando o numero da metade do intervalo, João sempre ganha 
algum valor

50 --> se maior, testar 75; menor testar 25
maior 50 e menor 75 - testar 61
maior 50 e maior 75 - testar 88
menor 50 e maior 25 - testar 38
menor 50 e menor 25 - testar 13
E assim por diante 
"""

import random

def criar_sacola(n):
    sacola = []
    for _ in range(n):
        sacola.append(random.randint(1,5000))
        sacola.sort()
    return sacola

def jogar_sacola(sacola, numero):
    pago = 0
    recebido = 0
    while True:
        chute = int(input("Em que posição está o número? "))
        print(f"Na posição {chute} o valor é {sacola[chute]}, ", end = "")
        if sacola[chute] == numero:
            recebido += 10
            print(f"e pensei nesse número mesmo. Você o encontrou!")
            break
        elif sacola[chute] < numero:
            pago += 1
            print(f"mas pensei em um número maior")
        else:
            pago +=1
            print(f"mas pensei em um número menor")
        print()

    return recebido - pago 


def main():
    sacola = criar_sacola(100)  #sacola com 100 números também
    numero = random.choice(sacola)  #numero tirado por Diná
    ganho = jogar_sacola(sacola, numero)
    print(f"Ganhei {ganho} reais!!!")

main()