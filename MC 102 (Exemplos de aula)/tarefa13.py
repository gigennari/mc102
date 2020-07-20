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

