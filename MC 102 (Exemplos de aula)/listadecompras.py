""" Escreva um programa que leia uma sequência de valores de itens de compra
e mostre o valor da soma de todos os itens. 
O usuário deverá escrever o valor de cada item, um por linha.
Quando não houver mais itens o usário irá indicar esse fato escrevendo um número negativo """

""" entrada: 3.50, 5.00, 16.36, -1   saída:24.86"""


lista_compras = []
valor = float(input('Insira o valore do primeiro item: '))

while valor >= 0:
    lista_compras.append(valor)
    valor = float(input('Insira o valor do próximo item: '))

soma = 0.0
for valor in lista_compras:
    soma += valor
print(f'O valor total de sua compra é {soma}')
