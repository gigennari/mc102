import math


while True:
    operador = input()
    if operador == "+":
        num1 = float(input())
        num2 = float(input())
        soma = num1 + num2
        print(soma)
    elif operador == "-":
        num1 = float(input())
        num2 = float(input())
        diferenca = num1 - num2
        print(diferenca)
    elif operador == "*":
        num1 = float(input())
        num2 = float(input())
        produto = num1 * num2
        print(produto)
    elif operador == "sqrt":
        num1 = float(input())
        raiz = int(math.sqrt(num1))
        print(raiz)
    elif operador == "baskara":
        a = float(input())
        b = float(input())
        c = float(input())
        delta = b**2 - 4*a*c 
        if delta < 0:
            print("Não tem raiz real")
            continue          #se usar break sai do while, se não usar contínuo dá erro, pois teremos divisor 0
        elif delta == 0:
            print("Há uma raiz real")
        else:
            print("Há duas raízes reais")
        x1 = (-b + math.sqrt(delta))/ 2*a 
        x2 = (-2 - math.sqrt(delta))/ 2*a
        print(f"As raízes reais são {x1} e {x2}.")
    elif operador == "F":
        break
    else: 
        print("Opeação inválida")


