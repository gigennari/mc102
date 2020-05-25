x, y = (input('Insira x e y: ')).split()

aux = x
x = y
y = aux 

print(x, y)


'''
Também poderiamos resolver dessa maneira:
x, y = y, x
print(x, y)

Ou ainda

x = x+y      
y = x-y      
x = x-y 
'''
