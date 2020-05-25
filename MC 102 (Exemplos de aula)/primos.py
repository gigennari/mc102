n = int(input())

encontrei_divisor = False
for i in range(2,n):
    print(f"Dividindo por {i}")
    if n % i ==0:
        encontrei_divisor = True
        break
if not encontrei_divisor and n>1:
    print(f"O número {n} é primo.")
else:
    print(f"O número {n} não é primo.")
    