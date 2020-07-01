""" Uma pergunta fundamental é um expressão aritmética com dois 
operandos inteiros não negativos, cujas operações permitidas são
soma (+), subtração(-), multiplicação (*) e divisão (/) e que 
cujo resultado é 42. Escreva um programa que só termine quando 
o usuário digitar uma pergunta fundamental (um operando, um
operador aritmético e outro operando).

   
"""


def separar_partes_operacao(variavel): #igual a funcao .spĺit() 
    partes = []
    pos_ultimo_espaco = -1
    i = 0
    n = len(variavel)
    while i < n:
        if variavel[i] == ' ':
            parte = variavel[pos_ultimo_espaco+1 : i]
            partes.append(parte)
            pos_ultimo_espaco = i
        i += 1
            
    parte = variavel[pos_ultimo_espaco+1 : n]
    partes.append(parte)
    return partes 


def realizar_operacao(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    if operador == '/':
        return num1 / num2
   



def main():
    resultado = 0
    while resultado != 42:
        operacao = input('Digite uma pergunta fundamental: ') #o input sempre devolve uma string 
        partes = separar_partes_operacao(operacao)
        operando1 = int(partes[0])
        operando2 = int(partes[2])
        operador = partes[1]
        resultado = realizar_operacao(operando1, operando2, operador)
        print('Essa não é uma pergunta fundamental.\n')         
    print('Obrigado! Essa é uma pergunta fundamental')
    

main()
