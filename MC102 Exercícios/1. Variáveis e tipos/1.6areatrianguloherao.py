a, b, c = input('Insira os três lados do triângulo:').split()

a = float(a)
b = float(b)
c = float(c)

import math

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print('A área do triângulo é '+ str(area) + 'u².')

""" 
Note que o programa não trabalha a condição de existência do triângulo. 
Logo, o prgrama pode calcular uma área de um triângulo que não existe.
"""