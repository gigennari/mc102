sequencia = [1] * 5
i = 1
while i < 10:
    breakpoint()
    sequencia[i] = sequencia[i - 1] * i
    i += 1
print(sequencia)
