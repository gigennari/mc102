A = input().split()
B = input().split()
C = []

for i in range(0,len(A)):
    j = A[i]+B[i]
    C.append(j)

for i in C:
    print(i, end=" ")
