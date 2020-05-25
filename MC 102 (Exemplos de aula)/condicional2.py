numero = int(input())

par = numero % 2 == 0
maior_10 = numero > 10
menor_50 = numero < 50

if par and maior_10:
    print("sim")
elif not par and menor_50:
    print("sim")
else:
    print("não")


