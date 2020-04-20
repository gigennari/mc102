# lê uma string com três partes
a, b, c = (input())
lista = [a, b, c]
lista.sort()
x, y, z = str(lista).replace(',',' ').replace('\'',' ').strip("[]").split()

# converte strings em números
x = float(x)
y = float(y)
z = float(z)


# termine esse programa aqui...

if (x ** 2)+(y ** 2) == (z ** 2):
	print('retângulo')
elif (x ** 2)+(y ** 2) < (z ** 2) and x+y>z:
	print('acutângulo')
elif (x ** 2)+(y ** 2) > (z ** 2) and x+y>z:
 	print('obstusângulo')
else:
	print('não forma triângulo')
