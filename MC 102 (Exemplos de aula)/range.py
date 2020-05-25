for i in range(5,11):
    for j in range(10-i):
        print("  ", end="")
    for j in range(2*i):
        print("*", end="")
    for j in range(10-i):                 #o código faz a mesma coisa sem essa linha?
        print("  ", end="")
    print()

    """"""