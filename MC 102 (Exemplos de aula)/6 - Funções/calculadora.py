"""Escreva uma caculadora que realiza soma e subtração. 
Uma instrução começa com o operador e uma linha seguido 
de duas linhas com os operandos.
O programa deve executar quantas operações forem fornecidas 
pelo usuário, que digitá F quando quiser terminar."""

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
    elif operador == "F":
        break
    else: 
        print("Opeação inválida")
