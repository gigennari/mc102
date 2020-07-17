"""
Escreva um programa para simular o seguinte jogo de azar:

Diná pensou em número entre 0 e 99
Joao vai tentar acertar

Se joao acertar, ele ganha 10 reais; se errar, paga 1 real
 
Queremos saber a chance de Joao ganhar ou perder esse jogo 

"""

import random

def jogar(numero):
    pago = 0
    recebido = 0
    while True:
        chute = int(input("Qual é o seu chute? "))  #recebe chute do João
        if chute == numero:
            recebido += 10
            print(f"O número é o {chute}. Você acertou!")
            break
        else:
            pago += 1
            print(f"Não é o {chute}.")
    
    return recebido - pago 

def main():
    numero = random.randint(0,99)   #devolve um num aleatório entre 0 e 99, num da Diná
    ganho = jogar(numero)   #pode ser negativo se ele só errar
    print(f"Ganhei {ganho} reais!!!") #a mensagem é otimista, mas em todas as vezes que joguei ganhei negativo hahaha

main()
