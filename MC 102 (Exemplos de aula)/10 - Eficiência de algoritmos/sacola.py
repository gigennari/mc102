"""
O novo jogo será o seguinte:
João dará uma sacola com alguns números para Diná, ele conhece os 
100 numeros que variam de 1 a 5000
Ela escolhe 1 e ele tem que acertar 


"""

import random 

def criar_sacola(n):
    sacola = []
    for _ in range(n):
        sacola.append(random.randint(1,5000))
    return sacola
 
def jogar_sacola(sacola, numero):
    pago = 0
    recebido = 0
    for chute in sacola:
        if chute == numero:
            recebido += 10
            print(f"O número é o {chute}. Você acertou!")
            break 
        else:
            pago += 1
            print(f"O numero não é o {chute}.")

    return recebido - pago

def main():
    sacola = criar_sacola(100)  #sacola com 100 números também
    numero = random.choice(sacola)  #numero tirado por Diná
    ganho = jogar_sacola(sacola, numero)
    print(f"Ganhei {ganho} reais!!!")

main()