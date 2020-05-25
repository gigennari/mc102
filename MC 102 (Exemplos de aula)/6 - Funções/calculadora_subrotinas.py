""" Criar subrotinas para realiar operações
Entrada:
operador
numero
numero""" 

import math

def operacao_soma():
    num1 = float(input())
    num2 = float(input())
    soma = num1 + num2
    print(soma)

def operacao_diferenca():
    num1 = float(input())
    num2 = float(input())
    diferenca = num1 - num2
    print(diferenca)

def operacao_produto():
    num1 = float(input())
    num2 = float(input())
    produto = num1 * num2
    print(produto)

def operacao_raiz():
    num1 = float(input())
    raiz = int(math.sqrt(num1))
    print(raiz)

def operacao_baskara():
    a = float(input())
    b = float(input())
    c = float(input())
    delta = b**2 - 4*a*c 
    if delta < 0:
        print("Não tem raiz real")
        return    #retorna ao lugar de origem, pŕoxima operação da função           
    elif delta == 0:
        print("Há uma raiz real")
    else:
        print("Há duas raízes reais")
    x1 = (-b + math.sqrt(delta))/ 2*a 
    x2 = (-2 - math.sqrt(delta))/ 2*a
    print(f"As raízes reais são {x1} e {x2}.")
    

def main():
    while True:
        operador = input()
        if operador == "+":
            operacao_soma()
        elif operador == "-":
            operacao_diferenca        
        elif operador == "*":
            operacao_produto()    
        elif operador == "sqrt":
            operacao_raiz()
        elif operador == "baskara":
            operacao_baskara()
        elif operador == "F":   
            break
        else: 
            print("Opeação inválida")

main()


