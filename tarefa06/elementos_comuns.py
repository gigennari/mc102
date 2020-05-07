A = (input()).split()
B = (input()).split()
C = []

for i in A:
    if i in B:
        C.append(i)
    else: 
        pass

D = []                    #crio uma nova lista para adicionar os valores de C, sem que eles se repitam   
for j in C:
    if j not in D:
        D.append(j)
    else:
        pass
print(str(D).replace('\'', ' ').replace(',', ' ').replace('[',' ').replace(']', ' '))

