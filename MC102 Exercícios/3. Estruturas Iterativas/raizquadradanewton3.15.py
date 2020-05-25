y = float(input("Insira o radicando: "))

x = y/2

for i in range(20):
    xnmais1 = (x ** 2 + y) / (2 * x)
    x = xnmais1


print(f"A raíz de {y} é aproximadamente {x:.3f}")