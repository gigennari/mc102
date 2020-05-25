r = int(input('Insira o raio do circulo: '))

import math
area = math.pi * (r**2)
perimetro = 2*math.pi*r

print('A área do circulo é ' + str(area))
print('O perimetro é ' + str(perimetro))