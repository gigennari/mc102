# lê uma string com três partes
a, b, c = (input()).split()

# converte strings em números
a = float(a)
b = float(b)
c = float(c)

lista = [a, b, c]
lista.sort()

# termine esse programa aqui...

if (lista[0]+lista[1]) > lista[2]:

	if ((lista[0] ** 2) + (lista[1] ** 2)) == (lista[2] ** 2):
		print('retângulo')

	elif ((lista[0] ** 2) + (lista[1] ** 2)) > (lista[2] ** 2): 
		print('acutângulo')

	elif ((lista[0] ** 2) + (lista[1] ** 2)) < (lista[2] ** 2): 
	 	print('obtusângulo')
else:
	print('não forma triângulo')
