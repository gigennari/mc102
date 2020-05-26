lista = input().split()

for i in range(len(lista)):
    lista[i] = int(lista[i])

print(lista)
print(type(lista))
print(type(lista[0]))